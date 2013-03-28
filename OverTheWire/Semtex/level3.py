#!/usr/bin/env python

import itertools

m1 = [   5,   2,  1,   7,   5 ]
m2 = [  13,  -7, -4,   1,   5 ]
m3 = [   9,  12,  9,  70,  -4 ]
m4 = [ -11,   9,  0,   5, -13 ]
m5 = [   4,  17, 12,   9,  24 ]
m6 = [  11, -17, 21,   5,  14 ]
m7 = [  15,  31, 22, -12,   3 ]
m8 = [  19, -12,  4,   3,  -7 ]
modifiers = [ m1, m2, m3, m4, m5, m6, m7, m8 ]

def successcheck():
  global v1, v2, v3, v4, v5

	if v1 != 400:
		return 0
	if v2 != 400:
		return 0
	if v3 != 400:
		return 0
	if v4 != 400:
		return 0
	if v5 != 400:
		return 0
	print "Success!"
	return 1

def applytransformation(trans):
	global v1, v2, v3, v4, v5, modifiers
	trans = modifiers[trans]
	v1 = v1 + trans[0]
	v2 = v2 + trans[1]
	v3 = v3 + trans[2]
	v4 = v4 + trans[3]
	v5 = v5 + trans[4]

def check(subset):
	for sub in subset:
		applytransformation(sub)
	if successcheck() == 1:
		print subset
	
for i in range(1,100):
	for subset in itertools.combinations_with_replacement(range(0,8) , i):
		#print subset
		v1 = 300
		v2 = 300
		v3 = 300
		v4 = 300
		v5 = 300
		check(subset)
