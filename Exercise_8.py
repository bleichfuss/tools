# Exercise 8
# author: Dominik Wirsig (XXXXXXX)
# Average, enter numbers and the program will calculate the average

s = 0.0 # sum
c = 0 # counter
while True:
	n = input('Enter a number (S to stop): ')
	if n == 's':
		break
	n = float(n)
	s += n
	c += 1
print('average value = ', s/c)
