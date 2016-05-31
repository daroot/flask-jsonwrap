import pytest
import simplejson as json

from flask import Flask, abort, jsonify
from flask_jsonwrap import JSONWrap
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse


def simple_app():
    """
    Very simple WSGI app.
    """
    thisapp = Flask('simpleapp')

    @thisapp.route('/')
    def root():
        return jsonify({'spam': 'eggs'})

    @thisapp.route('/parrot')
    def explode():
        abort(500)

    return thisapp


@pytest.fixture(scope="session")
def wrapped_client():
    wrapper = JSONWrap()
    wrapped = wrapper.init_app(simple_app())
    client = Client(wrapped, BaseResponse)
    return client


@pytest.fixture(scope="session")
def unwrapped_client():
    client = Client(simple_app(), BaseResponse)
    return client


@pytest.mark.parametrize('path, code, expected_wrapped, expected_unwrapped', [
    ('/', 200, {'spam': 'eggs'}, '{\n  "spam": "eggs"\n}'),
    ('/fjords', 404,
     {'errors': [{'status': '404: Not Found'}]},
     '<h1>Not Found</h1>'),
    ('/parrot', 500,
     {'errors': [{'status': '500: Internal Server Error'}]},
     '<h1>Internal Server Error</h1>'),
])
def test_wrapped_responses(wrapped_client, unwrapped_client, path, code,
                           expected_wrapped, expected_unwrapped):
    """
    When errors happen in a wrapped WSGI app, they should emit json messages
    with the appropriate status code attached.  Unwrapped WSGI apps return
    HTML based bodies.
    """
    unwrapped = unwrapped_client.get(path)
    wrapped = wrapped_client.get(path)

    assert unwrapped.status_code == code
    assert expected_unwrapped in unwrapped.data
    assert wrapped.status_code == code
    assert expected_wrapped == json.loads(wrapped.data)
