# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_cache import Cache
from flask_log import Logging

cache = Cache()
log = Logging()
