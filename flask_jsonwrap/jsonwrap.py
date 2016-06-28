from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


class JSONWrap(object):
    """
    Creates a JSONAPI-oriented Flask app.

    All error responses that you don't specifically manage yourself will have
    application/vnd.api+json content type, and will contain JSON like this
    (just an example):

    { "errors": [ { "message": "405: Method Not Allowed" } ] }

    Adapted from http://flask.pocoo.org/snippets/83/,
    listed in the public domain.
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def make_json_error(self, ex):
        code = ex.code if isinstance(ex, HTTPException) else 500
        errors = [{
            'status': str(ex),
        }]
        response = jsonify(errors=errors)
        response.status_code = code
        response.mimetype = 'application/vnd.api+json'
        return response

    def init_app(self, app):
        for code in default_exceptions.keys():
            app.register_error_handler(code, self.make_json_error)

        return app
