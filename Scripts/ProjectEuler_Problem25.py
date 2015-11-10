# Project Euler

import math


def numberOfDigits(integer):
	digits = 1;
	if(integer != 0):
		digits = int(math.log10(abs(integer)))+1
	return digits

def fib(n):
	if n == len(fibArray):
		return 1
	elif n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

class fibObject:
	"""docstring for fibObject"""
	def __init__(self):
		self.fibArray = [1,1]

	def fib(self,term):
		if term == 1:
			return self.fibArray[0]
		elif term == 2:
			return self.fibArray[1]
		elif term < len(self.fibArray)+1:
			return self.fibArray[term-1]
		else:
			n1 = self.fib(term-1)
			n2 = self.fib(term-2)
			rFib = n1 + n2
			self.fibArray.append(rFib)
			return rFib

	def main(self,digits):
		term = 0
		totalDigits = 1
		while (totalDigits < digits):
			term += 1
			result = self.fib(term)
			totalDigits = numberOfDigits(result)
		
		return term

project = fibObject()
print 	project.main(1000)	


