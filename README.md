# x-men-origins
:fax: A web app to ease cross origin requests for AJAX requests

Visit the [website](https://x-men-origins.herokuapp.com/)


# Installation
```
> pip install -r requirements.txt
```

# Usage
```
> FLASK_APP=web/__init__.py flask run # this will run at port 5000 by default
# or
> gunicorn web:app # this at 8000
```
Go to url `http://localhost:8000/cors?url=<url>`.

There is a form to use at `http://localhost:8000/`

Enjoy
