# Exercise 9
# author: Dominik Wirsig (XXXXXXX)
# Sierpinski Triangle, enter a number between 1 and 7 and the program will draw the Sierpinski Triangle for that number

import math, string

k = int(input('input k (will produce triangle with 2^k lines): '))
l = '' # output lines
n = 2**k # number of lines
for i in range(0, n):
	# last line should be printed left-aligned, that means first line is indented 2^k times
	for p in range(i, n):
		l += ' '
	# mark the odd numbers
	for j in range(0, i + 1):
		if(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)) % 2 == 1): # odd
			l += '* '
		else:
			l += '  '
	l += '\n'
print(l)


