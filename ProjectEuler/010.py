#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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

sum = 0

for p in primes:
	if p < 2000000:
		sum += p
	else:
		break

print sum

# passed