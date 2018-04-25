# x-men-origins
:fax: A web app to ease cross origin requests for AJAX requests

Visit the [website](https://x-men-origins.herokuapp.com/)

# Changelog
## v0.2.0
- Url changed from `/cors?url=<url>` to `/cors/<url>`
- Backward compatibility present

# Using with AJAX

```js
// using jquery get for example
$.get('https://x-men-origins.herokuapp.com/cors/https://google.com')
.then(function(data) {
    console.log(data);
});
```

# Development

## Installation
```sh
> pip install -r requirements.txt
```

## Usage
```sh
> FLASK_APP=web/__init__.py flask run # this will run at port 5000 by default
# or
> gunicorn web:app # this at 8000
```
Go to url `http://localhost:8000/cors/<url>`.

There is a form to use at `http://localhost:8000/`

![home page](https://github.com/shubhodeep9/x-men-origins/raw/master/.github/Screen%20Shot%202018-04-13%20at%202.54.18%20PM.png)

Enjoy
