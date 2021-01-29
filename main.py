from flask import Flask, render_template, jsonify, make_response, request
from os import getenv
from time import sleep
from random import randint

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Testing flask app', version='0.2')

UP = getenv("UP", True)
PORT = int(getenv("PORT", 5000))

@app.route("/")
def index():
    return "Uvodni stranka"

@app.route("/up")
@metrics.do_not_track()
def up():
    if up:
        return "OK"
    else:
        return make_response("Maintanance", 400)
    

@app.route("/url<int:id>")
def random_url_with_wait(id):
    wait_time = randint(1, int(id)+10) / 50
    sleep(wait_time)
    return f"Welcome at the great url {id} page. You waited {wait_time}s"

@app.route("/url<id>.json")
def random_url_with_wait_json(id):
    wait_time = randint(5, 150) / 100
    sleep(wait_time)
    _ret = {
            "msg": f"Welcome at the great url {id} page. You waited {wait_time}s",
            "wait_time": wait_time,
            "status": "ok",
            "requested_url": f"/url{id}.json"
        }
    r = make_response(jsonify(_ret), 200)
    r.content_type = "application/json"
    
    return r




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
