from flask import Flask
import socket

app = Flask(__name__)

@app.route("/bye")
def hello_world():
    return "<p>Bye, World from {}!</p>".format(socket.gethostname())
