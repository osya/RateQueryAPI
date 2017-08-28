#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rate_query_api.database import Column, String, Integer, Model


class Resource(Model):
    alias = Column(String)
    resource_id = Column(Integer)
    rate_table_id = Column(Integer)
