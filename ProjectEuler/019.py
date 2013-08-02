#!/usr/bin/env python

# You are given the following information, but you may prefer to do some
# research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

years = 2000 - 1901

days = 0
for i in range( 1900, 2001 ):
	days += 365
	if i % 4 == 0 and ( i % 100 != 0 or i % 400 == 0 ):
		days += 1
		print "Leap year"
	print i

print days
