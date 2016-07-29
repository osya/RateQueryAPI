#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, current_app
import telnetlib
import json

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

    res = res[res.find(nl) + len(nl):]
    res = [e.replace('rate_finder', '').strip() for e in res.split(nl) if not e.endswith('N/A')]

    res2 = []
    cur = current_app.cn.cursor()
    for line in res:
        l = line.split(',')
        if len(l) >= 2 and current_app.cn:
            trunk_id = l[0]
            cur.execute("""SELECT alias, resource_id FROM resource WHERE rate_table_id=%s""" % trunk_id)
            cf = cur.fetchone()
            if cf:
                l.insert(1, cf[0])
        res2.append(','.join(l))
    return json.dumps(res2)


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