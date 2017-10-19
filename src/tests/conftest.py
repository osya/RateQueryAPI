# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""
import pytest

import telnetlib
from flask_webtest import TestApp
from injector import Module, provider, singleton
from rate_query_api.app import create_app
from rate_query_api.commands import values
from rate_query_api.extensions import db as _db
from rate_query_api.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app(mocker):
    """An application for the tests."""

    class MockTelnetModule(Module):
        @provider
        @singleton
        def provide_telnet(self) -> telnetlib.Telnet:
            telnet = telnetlib.Telnet()
            mocker.patch.multiple(telnet, write=mocker.DEFAULT, read_until=mocker.DEFAULT)
            telnet.write.return_value = None
            mocker.patch.object(telnet, 'read_until')
            telnet.read_until.return_value = '\r\nrate_finder 1, 139\r\nend#'

            return telnet

    _app = create_app(TestConfig, binds=[MockTelnetModule])
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def test_app(app):
    """A Webtest app."""
    return TestApp(app, )


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    values()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()
