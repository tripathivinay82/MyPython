# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:28:24 2020

@author: vinayt
"""

from pprint import pprint
from jnpr.junos import Device

with Device(host='10.49.167.135', user='regress', password='MaRtInI' ) as dev:
    pprint( dev.facts )
