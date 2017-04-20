__author__ = 'spousty'


from bottle import route, run, get, post, DEBUG

import os
import socket
import random

#import math

#sorted([math.cos((random.random()*random.random()*2.3))/1.34 for i in range(2000000)])


@route('/')
def index():
   
    host = socket.gethostname()
    # Green - #008000
    # Blue - #0000FF
    # Red - #FF0000
    response_string = "<html> <style> body {background-color: #008000;} </style> <body> <h1> <font color='white'> Coming from Green on: " + str(host)+ " </font> </h1> </body> </html>"
    return response_string


if __name__ == '__main__':
	run(host='0.0.0.0', port=8080, debug=True)
