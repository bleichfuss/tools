# Exercise 11
# author: Dominik Wirsig (XXXXXXX)
# Class ZmodnZ, a class for the mathematical ring

class ZmodnZ:
	n = int
	value = int
	def __init__(self, n0 = 0, v = 0):
		self.n = n0
		self.value = v % n0
		
	def getValue(self):
		return self.value
		
	def __add__(self, b):
		if self.n != b.n:
			raise Exception('the operands have different moduli')
		else:
			return ZmodnZ(self.n, (self.value + b.value) % self.n)
	
	def __mul__(self, b):
		if self.n != b.n:
			raise Exception('the operands have different moduli')
		else:
			return ZmodnZ(self.n, (self.value * b.value) % self.n)
	
	def __str__(self):
		return 'ring Z/' + str(self.n) + 'Z: value = ' + str(self.value)

