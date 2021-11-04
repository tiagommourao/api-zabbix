#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima
#ajustado para adicionar host como SNMP
#colocado mais campos no CSV para atender a minha necessidade.

from pyzabbix import ZabbixAPI
import csv
from progressbar import ProgressBar, Percentage, ETA, ReverseBar, RotatingMarker, Timer

zapi = ZabbixAPI("http://172.16.1.162")
zapi.login(user="Admin", password="C113r#2021")

arq = csv.reader(open('/tmp/hosts.csv'))

linhas = sum(1 for linha in arq)

f = csv.reader(open('/tmp/hosts.csv'), delimiter=';')
bar = ProgressBar(maxval=linhas,widgets=[Percentage(), ReverseBar(), ETA(), RotatingMarker(), Timer()]).start()
i = 0

for [hostname,ip,dns,desc] in f:
    hostcriado = zapi.host.create(
        host= hostname,
        name= desc,
        description= desc,
        inventory_mode= 1,
        status= 1,
        interfaces=
        [{
            "type": "2",
            "main": "1",
            "useip": 1,
            "ip": ip,
            "dns": dns,
            "port": 161,
            "details":
                {
                "version": 2,
                "community": "{$SNMP_COMMUNITY}",
                "interface_ref": "if1"
                }
        }],
        groups=
        [{
            "groupid": 22
        }],
        templates=
        [{
            "templateid": 10249
        }]
    )


    i += 1
    bar.update(i)

bar.finish
print (" ")
