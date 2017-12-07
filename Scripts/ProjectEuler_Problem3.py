# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# URL: projecteuler.net/problem=3
# Username: Arjun.Kiran

import math

PRIMES = [2]
PRIME_FACTORS = []

# returns true if number is divisible by div
def isDivisible(number,div):
    return (number % div == 0)

def isPrime(number):
    global PRIMES
    bReturn = True
    # if the number is not already in the PRIMES list then evaluate the number
    if number not in PRIMES: 
        # evaluates number against existing known PRIMES
        for p in PRIMES:
            if isDivisible(number,p):
                bReturn = False
                break
                
        if bReturn == True:
            PRIMES.sort()
            # This number may be an undiscovered prime
            # must evaluate all numbers between the largest(plus one) known prime to number in question divided by two
            for p in xrange(PRIMES[-1]+1,number/2):
                if isDivisible(number,p):
                    bReturn = False
                    break
                    
            if bReturn == True:
                PRIMES.append(number)
                
    return bReturn 
    
##***** borrowed code    
def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step
##*****



def recursive_factors(number):
    global PRIME_FACTORS
    for n in xrange(2,number):
        if isDivisible(number,n)  and isPrime(n):
            PRIME_FACTORS.append(n)
            new_number = number/n
            if isPrime(new_number):
                # this is the recursive break
                PRIME_FACTORS.append(new_number)
            else:
                # the new number is not prime but worthy splitting off to find its prime factors
                recursive_factors(new_number)
            break
      
    
            

        
def main():
        number = 600851475143
        print number
        recursive_factors(number)
                
        PRIME_FACTORS.reverse()
        print PRIME_FACTORS[0]
        
if __name__ == '__main__':
    main()

