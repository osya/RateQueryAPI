#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import current_app
from flask_script import Manager

from rate_query_api.models import Resource

manager = Manager(usage='Commands for database data initialization')


@manager.command
def values():
    """ Main method for init data in database """
    with current_app.app_context():
        current_app.logger.info('Creating Resources...')
        Resource.create(id=1, alias='my_alias', resource_id=1, rate_table_id=1)
        Resource.create(id=2, alias='my_alias2', resource_id=1, rate_table_id=2)
    current_app.logger.info('Success. All initial data is loaded.')
