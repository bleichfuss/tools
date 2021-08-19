# Test script for Exercise 10
# author: Dominik Wirsig (XXXXXXX)
# test script to check the cg mehtod

from Exercise_10 import *

print('seed = 1')
x = cg(1)
for i in range(0, 100):
	print(next(x))

print('\nseed = 100')
y = cg(100)
for i in range(0, 100):
	print(next(y))
