#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

values = [ 11, 12, 13, 14, 16, 17, 18, 19, 20 ];

def divisible( i ):
	if not all( i % n == 0 for n in values ):
		return False
	return True

i = 20

while not divisible( i ):
	i += 20 # The number must be divisible by 20, so we can assume steps of 20

print i

# I'm pretty sure the point of this challenge is to see whether people
# realise that you don't need to check EVERY number between 1 and 20. If a
# number is divisible by 20, it will also be divisible by 2, etc

# passed