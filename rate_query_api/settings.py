# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import os.path as op


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('RATE_QUERY_API_SECRET', 'rate-secret-key')
    APP_DIR = op.abspath(op.dirname(__file__))  # This directory
    PROJECT_ROOT = op.abspath(op.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    TELNET_HOST = '192.168.99.100'
    TELNET_PORT = '23'
    TELNET_TIMEOUT = 2
    TELNET_USER = 'root'
    TELNET_PASSWORD = 'root'


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
