from flask import Flask, request, render_template
import subprocess
import gunicorn

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello, TheNewStack readers!\n'

@app.route("/dzone")
def bonjour():
    return "Hello, Dzone readers!\n"

