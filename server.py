from flask import Flask, request
from flask_cors import CORS
from json import dumps
from os import path, getcwd
from planning import plan

app = Flask(__name__, static_url_path='', static_folder='build')
CORS(app)


@app.route("/")
def react_app():
    return app.send_static_file('index.html')


@app.route("/api", methods=["POST"])
def calendar_planning():
    json = request.get_json()
    return dumps(plan(**json))
