
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# URL: projecteuler.net/problem=1
# Username: Arjun.Kiran

import math



    
if __name__ == '__main__':
	# calculating the max number divisible by 3 100
	threeLimit = (1000 - 1000%3)/3
	sum = 0
	for i in xrange(0,threeLimit+1):
	    sum += i*3

	# calculating the max number divisible by 5 under 1000 
	fiveLimit = (1000 - 1000%5)/5

	for j in xrange(0,fiveLimit):
		# this if statement is to insure that common multiples 
		# between 3 and 5 are not double counted 
	    if(j*5%3 != 0):
	        sum += j*5
	print sum
    
    
