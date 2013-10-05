# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial n
	return (1..n).inject(:*)
end

x = factorial 100
x = x.to_s

total = 0

x.each_char do |i|
	total += i.to_i
end

puts total

# passed