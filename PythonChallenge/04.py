#!/usr/bin/env python

import urllib2

base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = 63579

resp = "and the next nothing is "

while "and the next nothing is " in resp:
  conn = urllib2.urlopen(base + str(nothing))
	resp = conn.read()
	nothing = int(resp.replace('and the next nothing is ',''))
	print nothing

conn.close()
