# Exercise 10
# author: Dominik Wirsig (XXXXXXX)
# Linear Congruential Generator to create random numbers

def cg(seed):
	while True:
		seed = (1103515245 * seed + 12345) & (2**31 - 1)
		yield seed 
