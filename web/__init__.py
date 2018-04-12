from flask import Flask, request, abort
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def __fetch(url="https://ambitionbox.com"):
    try:
        r = requests.get(url)
        return {
                "status": r.status_code,
                "body": r.text
            }
    except:
        return {
                "status": 500,
                "body": ""
                }


@app.route("/cors")
def cross():
    url = request.args.get('url')
    r = __fetch(url)
    if(r["status"] != 200):
        abort(r["status"])

    return r["body"]

@app.route("/")
def index():
    return """
<h1>Welcome to X-Mens-Origins</h1>
<form action="/cors">
<input type="text" name="url">
<input type="submit">
</form>
    """
