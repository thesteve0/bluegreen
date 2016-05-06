__author__ = 'spousty'


from bottle import route, run, get, post, DEBUG
import os
import socket

@route('/')
def index():
    host = socket.gethostname()
    return "<h1> hello blue on: " + str(host)+ " </h1>"


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)