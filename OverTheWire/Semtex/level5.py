#!/usr/bin/env python

import socket, socks, struct

successes = 0
sockets = []

print "* Testing proxy list..."

def xor(s):
  out = ""
	key = 'HELICOTRMA'
	for i in xrange(0, len(s)):
		out += chr(ord(s[i]) ^ ord(key[i % len(key)]))
	return out

with open('proxies.txt') as f:
	for line in f:
		proxy = line.split(':')
		s = socks.socksocket()
		s.settimeout(5)
		s.setproxy(socks.PROXY_TYPE_SOCKS5,proxy[0],int(proxy[1]))
		print "Testing " + proxy[0] + ":" + proxy[1]
		try:
			s.connect(("semtex.labs.overthewire.org", 24027))
			s.settimeout(None)
			data = s.recv(4096)
		
			xored = xor(data)
			xored = xored + 'otisboxcar'
		
			s.sendall(xored)
			if data != "":
				print "Got " + data
				print "Sending " + xored
				successes = successes + 1
				print "Successes: " + str(successes)
				sockets.append(s)
			if successes == 10:
				print "Looping through sockets"
				count = 1
				for soc in sockets:
					print str(count) + ": " + soc.recv(4096)
					count = count + 1
				sys.exit(1)
		except:
			print "Connection failed"

f.close()
