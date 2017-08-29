# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_cache import Cache
from flask_log import Logging
from flask_sqlalchemy import SQLAlchemy, string_types


class MySQLAlchemy(SQLAlchemy):
    """
        Fixing the issue with missing `only` parameter in the Flask-SQLAlchemy's reflect() method
        Links:
            - https://stackoverflow.com/questions/23292931/flask-sqlalchemy-views-reflection
            - https://github.com/mitsuhiko/flask-sqlalchemy/issues/398
    """
    def _execute_for_all_tables(self, app, bind, operation, skip_tables=False, **kwargs):
        app = self.get_app(app)

        if bind == '__all__':
            binds = [None] + list(app.config.get('SQLALCHEMY_BINDS') or ())
        elif isinstance(bind, string_types) or bind is None:
            binds = [bind]
        else:
            binds = bind

        for bind in binds:
            extra = {}
            if not skip_tables:
                tables = self.get_tables_for_bind(bind)
                extra['tables'] = tables
            op = getattr(self.Model.metadata, operation)
            op(bind=self.get_engine(app, bind), **extra)

    def reflect(self, bind='__all__', app=None, **kwargs):
        self._execute_for_all_tables(app, bind, 'reflect', skip_tables=True, **kwargs)


cache = Cache()
log = Logging()
db = MySQLAlchemy()
