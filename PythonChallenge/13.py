#!/usr/bin/env python

import xmlrpclib

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.system.listMethods()

print server.system.methodHelp('phone') 
# Got: Returns the phone of a person

print server.phone('Bert')
