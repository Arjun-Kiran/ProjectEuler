# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# URL: projecteuler.net/problem=6
# Username: Arjun.Kiran
import math

def sum_squares(number):
    sum = 0
    for n in xrange(1,number+1):
        sum = n**2 + sum
        
    return sum
    
def squares_sum(number):
    sum = 0
    for n in xrange(1,number+1):
        sum = n + sum
        
    return sum**2
    
def main(number):
    return squares_sum(number) - sum_squares(number)

    
if __name__ == '__main__':
	print main(100)










