# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
from flask import url_for


class TestAPI:
    """Testing API."""

    def test_get_vendors_for_destination(self, testapp):
        res = testapp.get(url_for('api.get_vendors_for_destination', destination='US Virgin Islands Proper'))
        assert res.status_code == 200

    def test_get_vendor_rate(self, testapp):
        res = testapp.get(url_for('api.get_vendor_rate', vendor='US Virgin Islands Proper'))
        assert res.status_code == 200
