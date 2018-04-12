from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def __fetch(url="https://ambitionbox.com"):
    r = requests.get(url)
    return r.text

@app.route("/")
def index():
    url = request.args.get('url')
    return __fetch(url)
