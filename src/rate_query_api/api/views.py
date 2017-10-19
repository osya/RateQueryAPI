#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib

from flask import Blueprint, current_app, json, render_template

from rate_query_api.models import Resource

blueprint = Blueprint('api', __name__)


def exec_telnet_cmd(cmd, telnet: telnetlib.Telnet):
    timeout = current_app.config['TELNET_TIMEOUT']
    nl = '\r\n'
    telnet.write('login%s' % nl)
    telnet.write(str('%s%s' % (cmd, nl)))

    try:
        res = telnet.read_until('#', timeout=timeout)
    except EOFError as e:
        return 'Connection closed: %s' % e

    res = res[res.find(nl) + len(nl):]
    res = [e.replace('rate_finder', '').replace('end', '').strip() for e in res.split(nl) if not e.endswith('N/A')]

    res2 = []
    for line in res:
        line_split = line.split(',')
        if len(line_split) >= 2:
            el = {'id': line_split[0]}
            cf = Resource.query.filter_by(rate_table_id=line_split[0]).first()
            if cf:
                el['name'] = cf.alias
            el['rate'] = ','.join(line_split[1:])
            res2.append(el)
        else:
            line_strip = line.strip()
            if line_strip:
                res2.append(line_strip)

    return json.dumps(res2)


@blueprint.route('/api/v1/GetVendorsForDestination/<string:destination>', methods=['GET', 'POST'])
def get_vendors_for_destination(destination, telnet: telnetlib.Telnet):
    cmd = 'rate_finder_by_name 0,1,%s' % destination
    return exec_telnet_cmd(cmd, telnet)


@blueprint.route('/api/v1/GetVendorRate/<string:vendor>', methods=['GET', 'POST'])
def get_vendor_rate(vendor, telnet: telnetlib.Telnet):
    cmd = 'rate_finder_by_name 0,1,%s' % vendor
    return exec_telnet_cmd(cmd, telnet)


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    return render_template('public/home.html')


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')

# TODO: Use some Flask REST framework
