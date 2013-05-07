PyCON.tw 2013 deom scripts
======================
My demo programs in [PyCON.tw 2013](http://tw.pycon.org/2013/en/) Lightning Talk.

Violent Python: Python in the dark side.



Usage.
------

### bruteforce.py ###

a tool to generate brute force patters

    ./bruteforce.py aAdx 10

### decrypt.py ###

a dictionary attack tool to crack the UNIX 'crypt' encryption

    ./crypt_crack.py "$CRYPT" "$DICT_FILE"

    $ ./decrypt.py GGvxb.e7YgnIg /usr/share/dict/words
    [+] Found Password: egg(GGvxb.e7YgnIg)

### nmap-py.py ###

a python-nmap module demo code (need sudo permission)

    $ sudo ./nmap-py.py
    Password:
    {'nmap': {'scanstats': {'uphosts': u'1', 'timestr': u'Tue May  7 11:46:41 2013', 'downhosts': u'0', 'totalhosts': u'1', 'elapsed': u'3.53'}, 'scaninfo': {u'tcp': {'services': u'22-443', 'method': u'syn'}}, 'command_line': u'nmap -oX - -p 22-443 -sV 127.0.0.1'}, 'scan': {u'127.0.0.1': {'status': {'state': u'up', 'reason': u'localhost-response'}, 'hostname': u'localhost', 'addresses': {u'ipv4': u'127.0.0.1'}}}}
    
    ... (omitted)


### skype.py ###

a demo program to dump skype data

    $ ./skype.py ~/Library/Application\ Support/Skype/$account/main.db
    show tables:
    [(u'DbMeta',), (u'Contacts',), (u'LegacyMessages',), (u'Calls',), (u'Accounts',), (u'Transfers',),    (u'Voicemails',), (u'Chats',), (u'Messages',), (u'ContactGroups',), (u'Videos',), (u'SMSes',), (u'CallMembers',), (u'ChatMembers',), (u'Alerts',),     (u'Conversations',), (u'Participants',), (u'VideoMessages',)]
    
    
    Dump Account:
    --------------------------------------------------
    [*] -- Found Account --
        [+] User: xatier
        [+] Skype Username: ******
        [+] Location: HsinChu,tw
        [+] Profile Date: 2013-**-** 00:00:00
    
    
    Dump Contacts:
    --------------------------------------------------
    [*] -- Found Account --
        [+] User: Echo / Sound Test Service
        [+] Skype Username: echo123
        [+] Phone_mobile: None
        [+] Birthday: None
    
    ... (omitted)

Warning
-------

# do not use these scripts to do bad things!!! #

![Imgur](http://i.imgur.com/JQgSRgF.png)

Licensed
----------
Licensed under the [GPL license][GPL].
[GPL]: http://www.gnu.org/licenses/gpl.html
