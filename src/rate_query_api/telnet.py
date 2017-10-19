#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

import telnetlib
from injector import Module, provider, singleton


class TelnetModule(Module):
    @provider
    @singleton
    def provide_telnet(self, app: Flask) -> telnetlib.Telnet:
        host = app.config.get('TELNET_HOST')
        port = app.config.get('TELNET_PORT')
        return telnetlib.Telnet(host, port)
