#!/usr/bin/env python

# a = [1, 11, 21, 1211, 111221, 
# len(a[30]) = ?
# each number describes the previous, numerically
# eg 11 = one one = 1, 21 = two ones = 11

numbers = [1]

def nextnumber(number):
  num = str(number)
	last = ''
	count = 0
	next = ''
	for i in num:
		if i != last:
			next = next + str(count) + str(last)
			count = 1
			last = i
		else:
			count += 1
	next = next + str(count) + str(last)
	numbers.append(next[1:])
	return next[1:]

last = nextnumber(1)
while len(numbers) < 31:
	last = nextnumber(last)

print len(numbers[30])
#5808
