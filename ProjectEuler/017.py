#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

digits = dict()
digits[0] = ""
digits[1] = "one"
digits[2] = "two"
digits[3] = "three"
digits[4] = "four"
digits[5] = "five"
digits[6] = "six"
digits[7] = "seven"
digits[8] = "eight"
digits[9] = "nine"

tens = dict()
tens[1] = ""
tens[2] = "twenty"
tens[3] = "thirty"
tens[4] = "forty"
tens[5] = "fifty"
tens[6] = "sixty"
tens[7] = "seventy"
tens[8] = "eighty"
tens[9] = "ninety"

teens = dict()
teens[10] = "ten"
teens[11] = "eleven"
teens[12] = "twelve"
teens[13] = "thirteen"
teens[14] = "fourteen"
teens[15] = "fifteen"
teens[16] = "sixteen"
teens[17] = "seventeen"
teens[18] = "eighteen"
teens[19] = "nineteen"


def int_to_english( n ):
	if n == 1000:
		return "onethousand"
	elif n >= 100:
		answer = digits[n / 100]
		answer += "hundred"
		if n % 100 != 0:
			answer += "and"
		answer += int_to_english( n - (n/100)*100 )
		return answer
	elif n >= 20:
		answer = tens[n / 10]
		answer += int_to_english( n - (n/10)*10 )
		return answer
	elif n >= 10:
		answer = teens[n]
		return answer
	elif n in digits:
		return digits[n]

sum = 0
for i in range( 1, 1001 ):
	sum += len( int_to_english( i ) )
print sum

# passed