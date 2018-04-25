from flask import Flask, request, abort
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def __fetch(url="https://ambitionbox.com", params={}, user_agent=None):
    headers_Get = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    try:
        r = requests.get(url, params=params, headers=headers_Get)
        return {
                "status": r.status_code,
                "body": r.text
            }
    except:
        return {
                "status": 500,
                "body": ""
                }


@app.route("/cors/<path:url>")
def cross(url):
    user_agent = request.headers.get('User-Agent')
    r = __fetch(url, dict(request.args), user_agent)
    if(r["status"] != 200 and r["status"] != 503):
        abort(r["status"])

    return r["body"]

@app.route("/")
def index():
    return """
<center>
    <h1>Welcome to X-Men Origins</h1>

    <h2 style="font-weight: lighter">A web app to ease cross origin requests for AJAX requests</h2>

    <form action="/cors">
        <input type="text" name="url">
        <input type="submit">
    </form>
</center>
    """
