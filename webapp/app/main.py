from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World from {}!</p>".format(socket.gethostname())
