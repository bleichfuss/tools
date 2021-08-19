# Test script for Exercise 11
# author: Dominik Wirsig (XXXXXXX)
# script for testing the class

from Exercise_11 import *

a = ZmodnZ(8, 3)
b = ZmodnZ(8, 12)
c = ZmodnZ(7, 4)
d = ZmodnZ(8, -5)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
try:
	print('a + b = ', a + b)
	print('a * d = ', a * d)
	print('b + c = ', b + c)
except Exception as e:
	print('Error caught:', e)

