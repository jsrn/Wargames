#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/disproportional.html

import xmlrpclib

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()

print server.system.methodHelp('phone') 
# Got: Returns the phone of a person

print server.phone('Bert')
