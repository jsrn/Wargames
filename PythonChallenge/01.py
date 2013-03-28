#!/usr/bin/env python
# http://www.pythonchallenge.com/pc/def/map.html

a = "map"

b = ''

for ch in a:
  if ch.isalpha():
		if ch=='z':
			new = 'b'
		elif ch=='y':
			new = 'a'
		else:
			new = chr(ord(ch) + 2)

		b = b + new
		
	else:
		b = b + ch

print b
