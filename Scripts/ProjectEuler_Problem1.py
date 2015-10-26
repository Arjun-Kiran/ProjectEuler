
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# URL: projecteuler.net/problem=1
# Username: Arjun.Kiran

import math

three = 3
five = 5

threeLimit = (1000 - 1000%3)/3
sum = 0
for i in xrange(0,threeLimit+1):
    sum += i*3

fiveLimit = (1000 - 1000%5)/5

for j in xrange(0,fiveLimit):
    if(j*5%3 != 0):
        sum += j*5

    

print sum
    
    
