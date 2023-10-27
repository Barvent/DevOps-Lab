from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/bye")
def bye_world():
    os.system('ls')
    return "Bye! I am {} by the way.".format(socket.gethostname())
