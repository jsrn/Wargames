#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
	D = {}
	q = 2  # first integer to test for primality.
	while True:
		if q not in D:
			yield q 
			D[q * q] = [q] 
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

primes = gen_primes()

count = 1
for p in primes:
	if count == 10001:
		print p
		break
	count += 1

# pass