#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, render_template, current_app
import telnetlib

blueprint = Blueprint('api', __name__)


def exec_telnet_cmd(cmd):
    timeout = current_app.config['TELNET_TIMEOUT']
    nl = '\r\n'

    tn = telnetlib.Telnet(current_app.config['TELNET_HOST'], current_app.config['TELNET_PORT'])
    tn.write('login%s' % nl)
    tn.write('help%s' % nl)

    try:
        res = tn.read_until('#', timeout=timeout)
    except EOFError as e:
        return "Connection closed: %s" % e
    res = res.replace('\r\n', '<br/>')

    return res


@blueprint.route('/api/v1/GetVendorsForDestination', methods=['GET', 'POST'])
def get_vendors_for_destination():
    return exec_telnet_cmd('echo "Hello"')


@blueprint.route('/api/v1/GetVendorRate', methods=['GET', 'POST'])
def get_vendor_rate():
    return exec_telnet_cmd('ps')


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')