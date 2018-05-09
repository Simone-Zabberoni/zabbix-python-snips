#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Get all hosts, print the id and name 

You can provide an argument to filter a specific host
"""

from zabbix.api import ZabbixAPI
import sys

zabbixServer    = 'http://yousrserver/zabbix/'
zabbixUser      = 'someuser'
zabbixPass      = 'somepass'

zapi = ZabbixAPI(url=zabbixServer, user=zabbixUser, password=zabbixPass)


if (sys.argv[1:]):
    # Filter based on the cmdline argument
    f  = {  'host' : sys.argv[1:]  }
    hosts = zapi.host.get(filter=f, output=['hostids', 'host'] );
else:
    hosts = zapi.host.get(output=['hostids', 'host'] );


for host in hosts:
    print "ID: {} - Host: {}".format(host['hostid'], host['host'])

