__author__ = 'spousty'


from bottle import route, run, get, post, DEBUG
import os
import socket

@route('/')
def index():
    host = socket.gethostname()
    # Green - #008000
    response_string = "<html> <style> body {background-color: #0000FF;} </style> <body> <h1> <font color="white"> hello blue on: " + str(host)+ " </font> </h1> </body> </html>"
    return response_string


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)