from flask import Flask, render_template, jsonify, make_response, request, g
from os import getenv, path
import time
from random import randint

# SQLalchemy
from flask_sqlalchemy import SQLAlchemy

# Prometheus metrics
from prometheus_flask_exporter import PrometheusMetrics

# CORS
from flask_cors import CORS

# Prometheus metrics
from prometheus_flask_exporter import PrometheusMetrics

# GraphQL
from flask_graphql import GraphQLView
import schema
import graphene_prometheus

UP = getenv("UP", True)
PORT = int(getenv("PORT", 5000))
THREADED = bool(getenv("THREADED", True))
ENV = str(getenv("ENV", "devel"))
VERSION = "unknown"
DB_URI = str(getenv("DB_URI", "sqlite:///develop.sqlite3"))

try:
    with open("./VERSION") as ver:
        VERSION = ver.read().strip()

except IOError as err:
    print("Unable to find VERSION file, but continue...")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)

def checkDB():
    try:
        db.session.execute("select 1;")
        return True
    except:
        return False

# Set CORS for graphql
CORS(app, resources={r"/graphql/*": {"origins": "*"}})

# Configure metrics for prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Testing flask app', version=VERSION)

app.debug = True

@app.before_request
def start():
    g.start = time.time()

@app.after_request
def after(response):
    diff = (time.time() - g.start) * 1000
    print("Full exec time: %s" % str(diff))
    return response

@app.route("/")
def index():
    return """
        <html>
        <body>
        
        <H1> API responser </H1>
        
        <hr noshade>
        
        <H2>Friendly response to every request...</H2>

        <p>Api response delay simulator. There are many API endpoints generating randomly delayed response</p>

        <ul>
            <li><a href="/graphql" class="button" test-data="graphql-api">/graphql UI</a></li>
            <li><a href="/url1" class="button" test-data="rest-api-txt">/url${ID} REST text</a></li>
            <li><a href="/url1.json" class="button" test-data="rest-api-json">/url${ID}.json REST json</a></li>
        </ul>

        </body>
        </html>
    """

@app.route("/version")
def version():
    return VERSION

@app.route("/up")
@metrics.do_not_track()
def up():
    if up:
        return "OK"
    else:
        return make_response("Maintanance", 400)

@app.route("/status")
@metrics.do_not_track()
def status():
    _ret = {
        "db": checkDB(),
        "app": True,
        "port": PORT,
        "threaded": THREADED,
        "version": VERSION
    }
    r = make_response(jsonify(_ret), 200)
    r.content_type = "application/json"
    return r


@app.route("/url<int:id>")
def random_url_with_wait(id):
    wait_time = randint(1, int(id)+10) / 50
    time.sleep(wait_time)
    print("Done")
    r = make_response(f"Welcome at the great url {id} page. You waited {wait_time}s", 200)
    r.headers["X-Frame-Options"] = "SAMEORIGIN"
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.content_type = "text/plain"
    return r

@app.route("/url<id>.json")
@app.route("/api/<id>.json")
def random_url_with_wait_json(id):
    wait_time = randint(5, 150) / 100
    time.sleep(wait_time)
    _ret = {
            "msg": f"Welcome at the great url {id} page. You waited {wait_time}s",
            "wait_time": wait_time,
            "status": "ok",
            "requested_url": f"/url{id}.json"
        }
    r = make_response(jsonify(_ret), 200)
    r.headers["X-Frame-Options"] = "SAMEORIGIN"
    r.headers["X-Content-Type-Options"] = "nosniff"
    r.content_type = "application/json"
    print("Done")
    return r

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema.SCHEMA,
    pretty=True,
    graphiql=True
))



if __name__ == "__main__":
    # preparation for app with DB
    if not path.exists(DB_URI):
        db.create_all()
    
    app.run(host="0.0.0.0", port=PORT, threaded=THREADED)
