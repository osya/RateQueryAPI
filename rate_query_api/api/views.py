#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, render_template, current_app
import telnetlib

blueprint = Blueprint('api', __name__)


def exec_telnet_cmd(cmd):
    timeout = current_app.config['TELNET_TIMEOUT']
    nl = '\r\n'

    user = current_app.config['TELNET_USER']
    password = current_app.config['TELNET_PASSWORD']
    tn = telnetlib.Telnet(current_app.config['TELNET_HOST'], current_app.config['TELNET_PORT'])

    try:
        tn.read_until("login: ", timeout=timeout)
    except EOFError as e:
        return "Connection closed: %s" % e

    tn.write(user + nl)
    if password:
        try:
            tn.read_until("Password: ", timeout=timeout)
        except EOFError as e:
            return "Connection closed: %s" % e
        tn.write(password + nl)

    try:
        res = tn.read_until('#', timeout=timeout)
    except EOFError as e:
        return "Connection closed: %s" % e

    if 'Login incorrect' in res:
        return 'Login incorrect'

    tn.write("%s%s" % (cmd, nl))

    try:
        res = tn.read_until('#', timeout=timeout)
    except EOFError as e:
        return "Connection closed: %s" % e

    return res[res.find(nl) + len(nl):res.rfind(nl)]


@blueprint.route('/api/v1/GetVendorsForDestination', methods=['GET', 'POST'])
def get_vendors_for_destination():
    return jsonify({'Result': exec_telnet_cmd('echo "Hello"')})


@blueprint.route('/api/v1/GetVendorRate', methods=['GET', 'POST'])
def get_vendor_rate():
    return jsonify({'Result': exec_telnet_cmd('ps')})


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')