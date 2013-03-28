#!/usr/bin/env python

import binascii

w = open('binary', 'wb')

with open("garbage", "rb") as f:
  byte = f.read(1)
	while (byte != ""):
		binary_string = binascii.hexlify(byte)
		binary = bin(int(binary_string, 16))[2:]
		binary = int(binary,2)
		w.write('%c' % int(binary))
		f.read(1)
		byte = f.read(1)

f.close()
w.close()
