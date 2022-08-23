from flask import Flask
import socket

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, I am {}!".format(socket.gethostname())
