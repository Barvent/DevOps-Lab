from flask import Flask
import socket

app = Flask(__name__)

@app.route("/bye")
def bye_world():
    return "Bye! I am {} by the way.".format(socket.gethostname())
