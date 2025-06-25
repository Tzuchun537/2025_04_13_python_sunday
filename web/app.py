from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<H1>Hello, 好不好!</H1>'
