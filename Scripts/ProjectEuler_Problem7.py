# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
# URL: projecteuler.net/problem=7
# Username: Arjun.Kiran

import math
# Borrowed algorithm from my Project Euler Problem 3
PRIMES = [2]

def addPrimes(number):
    global PRIMES
    PRIMES.append(number)

def getPrimes():
    global PRIMES
    return PRIMES
 
def isDivisible(number,div):
    return (number%div == 0)

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
            addPrimes(number)
            # PRIMES.append(number)
                
    return bReturn 
    
    
def main(numberPrimes):
    global PRIMES
    n = 1
    while(len(PRIMES) < numberPrimes):
        # no need to count the even numbers. iterate only the odds
        n = n + 2
        isPrime(n)
        
    return PRIMES[-1]
    
if __name__ == '__main__':
    print main(10001)

        