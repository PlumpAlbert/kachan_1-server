from flask import Flask
from os import path, getcwd

app = Flask(__name__, static_url_path='', static_folder='build')


@app.route("/")
def react_app():
    return app.send_static_file('index.html')


@app.route('/create')
def lol():
    file = open('test', 'w')
    file.write('This is a test')
    return 200


@app.route('/get')
def get():
    file = open('test', 'r')
    return file.read()