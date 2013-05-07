#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3

def printProfile(skypeDB):
    conn = sqlite3.connect(skypeDB)
    c = conn.cursor()


    print "show tables:"
    c.execute("SELECT tbl_name from sqlite_master WHERE type=='table';")
    print c.fetchall()

    c.execute("SELECT fullname, skypename, city, country, \
               datetime(profile_timestamp,'unixepoch') FROM Accounts;")


    print "\n"
    print "Dump Account: "
    print "-" * 50
    for row in c.fetchall():
        print '[*] -- Found Account --'
        print '    [+] User: ' + row[0]
        print '    [+] Skype Username: ' + row[1]
        print '    [+] Location: ' + row[2] + ',' + row[3]
        print '    [+] Profile Date: ' + row[4]

    print "\n"
    print "Dump Contacts: "
    print "-" * 50
    c.execute("SELECT displayname, skypename, phone_mobile, \
               birthday FROM Contacts;")

    for row in c.fetchall():
        print '[*] -- Found Account --'
        print '    [+] User: ' + (row[0]).encode('utf8')
        print '    [+] Skype Username: ' + row[1]
        print '    [+] Phone_mobile: ' + str(row[2])
        print '    [+] Birthday: ' + str(row[3])


if __name__ == "__main__":
    printProfile(sys.argv[1])

# Usage: (OS X)
# ./skype.py ~/Library/Application\ Support/Skype/$account/main.db 
# 
# (Linux)
# ./skype.py ~/.Skype/$account/main.db 
