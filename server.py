from flask import Flask, request, send_file
from flask_cors import CORS
from mimetypes import guess_type
from json import dumps
from os import path, mkdir
from planning import plan

app = Flask(__name__, static_url_path='', static_folder='build')
CORS(app)

if not path.exists('docs'):
    mkdir('docs')

@app.route("/")
def react_app():
    return app.send_static_file('index.html')


@app.route("/api", methods=["POST"])
def calendar_planning():
    json = request.get_json()
    return dumps(plan(**json))

@app.route('/report/<path:subpath>')
def report(subpath):
    print('SUBPATH:', subpath)
    print('MIME:', guess_type(subpath))
    return send_file(subpath, mimetype=guess_type(subpath)[0], as_attachment=True)