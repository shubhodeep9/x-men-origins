from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def __fetch(url="https://ambitionbox.com"):
    r = requests.get(url)
    return r.text

@app.route("/")
def index():
    return __fetch()
