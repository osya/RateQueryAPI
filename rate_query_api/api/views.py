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
    tn.write(str('%s%s' % (cmd, nl)))

    try:
        res = tn.read_until('#', timeout=timeout)
    except EOFError as e:
        return "Connection closed: %s" % e
    return res[res.find(nl) + len(nl):].replace('\r\n', '<br/>')


@blueprint.route('/api/v1/GetVendorsForDestination/<string:destination>', methods=['GET', 'POST'])
def get_vendors_for_destination(destination):
    cmd = 'rate_finder_by_name 0,1,%s' % destination
    return exec_telnet_cmd(cmd)


@blueprint.route('/api/v1/GetVendorRate/<string:vendor>', methods=['GET', 'POST'])
def get_vendor_rate(vendor):
    cmd = 'rate_finder_by_name 0,1,%s' % vendor
    return exec_telnet_cmd(cmd)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')