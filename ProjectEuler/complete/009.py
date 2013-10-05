#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

for a in range( 500 ):
	for b in range( 500 ):
		if a < b:
			c2 = a**2 + b**2
			c = math.sqrt(c2)
			if a + b + c == 1000:
				print a * b * c

# passed