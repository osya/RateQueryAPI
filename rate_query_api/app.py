# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask, render_template
from rate_query_api import api
from rate_query_api.extensions import cache, log
from rate_query_api.settings import ProdConfig
import psycopg2


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    try:
        args = {
            'host': app.config['EGRESS_DB_HOST'],
            'port': app.config['EGRESS_DB_PORT'],
            'database': app.config['EGRESS_DB_NAME'],
            'user': app.config['EGRESS_DB_USER'],
            'password': app.config['EGRESS_DB_PASSWORD']
        }
        app.cn = psycopg2.connect(**args)
    except psycopg2.Error as e:
        app.logger.exception("Failed to connect to DB: {host: '%(host)s', port: %(port)d, db: '%(database)s',"
                             " user: '%(user)s'}" % args)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    cache.init_app(app)
    log.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(api.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
