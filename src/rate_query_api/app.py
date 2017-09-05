# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template
from flask_injector import FlaskInjector

from rate_query_api.api import views
from rate_query_api.extensions import cache, db, log
from rate_query_api.settings import ProdConfig
from rate_query_api.telnet import TelnetModule


def create_app(config_object=ProdConfig, binds=None):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param binds: List of injected modules
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    if binds is None:
        binds = [TelnetModule]
    FlaskInjector(app=app, modules=binds)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    cache.init_app(app)
    log.init_app(app)
    db.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.blueprint)
    return None


def register_error_handlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
