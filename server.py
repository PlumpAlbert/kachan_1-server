from flask import Flask
from os import path, getcwd

app = Flask(__name__, static_url_path='', static_folder='build')


@app.route("/")
def react_app():
    return app.send_static_file('index.html')
