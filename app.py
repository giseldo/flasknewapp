from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "ola mundo"

@app.route('/ola')
def ola():
    return "ola mundo novo"

@app.route('/novo')
def novo():
    return "ola mundo novo"


@app.route('/<name>')
def acao(name):
    return f"ola mundo novo{name}"