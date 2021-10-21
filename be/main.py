from flask import Flask, jsonify, make_response, request, g
from os import uname, getenv, path

# SQLalchemy
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

# Prometheus metrics
from prometheus_flask_exporter import PrometheusMetrics

# CORS
from flask_cors import CORS

INSTANCE = uname()[1]
ENV = str(getenv("ENV", "devel"))
PORT = int(getenv("PORT", 5001))
VERSION = "unknown"
THREADED = bool(getenv("THREADED", True))
DB_URI = str(getenv("DB_URI", "sqlite:///develop.sqlite3"))

try:
    with open("./VERSION") as ver:
        VERSION = ver.read().strip()

except IOError as err:
    print("Unable to find VERSION file, but continue...")



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)

# Configure metrics for prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Testing flask app', version=VERSION, instance=INSTANCE)

app.debug = True

# Set CORS for API
CORS(app, resources={r"/api/*": {"origins": "*"}})




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30)) 
    key = db.Column(db.String(250))

    def __repr__(self) -> str:
        return "<Name %s>" % self.name






def checkDB():
    try:
        db.session.execute("select 1;")
        return True
    except:
        return False


@app.route("/status")
@metrics.do_not_track()
def status():
    _ret = {
        "db": checkDB(),
        "app": True,
        "port": PORT,
        "version": VERSION
    }
    r = make_response(jsonify(_ret), 200)
    r.content_type = "application/json"
    return r


@app.route("/api/user/list.json")
def list_users():
    ret = [dict(name=i.name, key=i.key, id=i.id) for i in User.query.all()]
    r = make_response(jsonify(ret), 200)
    r.content_type = "application/json"
    return r


@app.route("/api/user/", methods = ["POST"])
@app.route("/api/user/<id>.json", methods = ["POST"])
def add_user(id = None):
    d = request.get_json(force=True)
    #if db.query.filter_ny(id=id).first()
    try:
        new_usr = User(id=id, name=d["name"], key=d["key"])
        db.session.add(new_usr)
        db.session.commit()
        ret = dict(status="Ok")
        r = make_response(jsonify(ret), 200)

    except sqlalchemy.exc.IntegrityError as err:
        print(f"User with id {id} already exists")
        ret = dict(status="Fail", message=f"User with id {id} already exists")
        r = make_response(jsonify(ret), 400)
        
    
    r.content_type = "application/json"
    return r


@app.route("/api/user/<id>.json")
def get_user(id):
    _ret = {
            "status": "ok",
            "version": VERSION,
            "instance": INSTANCE,
            "requested_url": f"/api/user/{id}.json",
            "data": {
                "name": "user_name"
            }
        }
    r = make_response(jsonify(_ret), 200)
    r.headers["X-Frame-Options"] = "SAMEORIGIN"
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.content_type = "application/json"
    return r

if __name__ == "__main__":
    # preparation for app with DB
    if not path.exists(DB_URI):
        db.create_all()
    
    app.run(host="0.0.0.0", port=PORT, threaded=THREADED)