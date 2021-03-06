# Project Euler Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
# NOT SOLVED:because it has a long execution time.  
import math, sys, os


def findDivisors(number):
	if number != 1:
		nDivisors = 2
	else:
		nDivisors = 1

	for i in xrange(2,number/2):
		if (number%i) == 0:
			nDivisors = nDivisors + 1

	return nDivisors

def triangleNumber(n):
	# can't use. is not scalable recursion 
	bReturn = 0 # placeholder value
	if n != 0:
		bReturn = n + triangleNumber(n-1)
	
	return bReturn

def main():
	nDivisors = 0
	nTerm = 0
	nTriangle = 0
	while(nDivisors < 500):
		nTerm = nTerm + 1
		nTriangle = nTriangle + nTerm
		nDivisors = findDivisors(nTriangle)

	print nTerm
	print triangleNumber(nTerm)

main()




