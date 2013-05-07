#!/usr/bin/python

import nmap
nm = nmap.PortScanner()
result = []
result.append( nm.scan('127.0.0.1', ports='22-443')   )
result.append( nm.scan('127.0.0.1', arguments='-p22-443')   )
result.append( nm.scan('localhost', arguments='-sT'))
result.append( nm.scan(arguments='-p 0-1024')       )
result.append( nm.scan(arguments='-p22 -sV')        )

for r in result:
    print r
    print "=" * 50

'''
methods:
nm.all_hosts             nm.get_nmap_last_output  nm.nmap_version          nm.scanstats
nm.command_line          nm.has_host              nm.scan
nm.csv                   nm.listscan              nm.scaninfo


nm.scan()
    Definition: nm.scan(self, hosts='127.0.0.1', ports=None, arguments='-sV')
    hosts = string for hosts as nmap use it 'scanme.nmap.org' or '198.116.0-255.1-127' or '216.163.128.20/20'
    ports = string for ports as nmap use it '22,53,110,143-4564'
    arguments = string of arguments for nmap '-sU -sX -sC'

maybe need root privileges
    PortScannerError: u'You requested a scan type which requires root privileges.\nQUITTING!\n'
'''
