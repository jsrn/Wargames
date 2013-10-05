#!/usr/bin/env python

# Starting in the top left corner of a 2x2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
# ------------------------------------------------------------------------------
# To get the number of solutions, we need to find the middle number of the 40th
# (0 indexed) row of Pascal's triangle
# Luckily, there is a way to calculate a row of Pascal's triangle on its own.

from __future__ import division

numerator = 40
denominator = 1

last = 1
top = 0

while numerator is not 1:
	last *= ( numerator / denominator )
	numerator -= 1
	denominator += 1
	if last > top:
		top = last
	else:
		print int(top)
		break

# passed