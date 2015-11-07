
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

    

print main(100)









