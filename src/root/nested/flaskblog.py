'''
Created on Mar 15, 2019

@author: almanzor
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
