#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0

def ispalindrome( n ):
	return str(n)[::-1] == str(n)

for i in range( 1, 1000 ):
	for j in range( 1, 1000 ):
		product = i * j
		if ispalindrome( product ):
			if ( product > largest ):
				largest = product

print largest

#passed