Flask-JSONWrap
==============

A Flask extension for wrapping errors in appropriate JSON-API compatible json.


Installation
------------

Install the extension using pip:

    $ pip install -U flask-jsonwrap


Usage
-----


This package exposes a Flask exentions which overwrites the default HTML error
handling endpoints in Flask with endpoints that return error messages in the
manner decribed by [JSON-API](http://jsonapi.org)


```python
    from flask_jsonwrap import JSONWrap

	app = Flask(__name__)
	jsonwrap = JSONWrap()
	jsonwrap.init_app(app)
```


Tests
-----

