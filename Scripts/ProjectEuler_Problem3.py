# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# URL: projecteuler.net/problem=3
# Username: Arjun.Kiran

import math

PRIMES = [2]
PRIME_FACTORS = []

def isPrime(number):
    global PRIMES
    bReturn = True
    # if the number is not already in the PRIMES list then evaluate the number
    if number not in PRIMES: 
        # evaluates number against existing known PRIMES
        for p in PRIMES:
            mod = number % p
            if mod == 0:
                bReturn = False
                break
                
        if bReturn == True:
            PRIMES.sort()
            # This number may be an undiscovered prime
            # must evaluate all numbers between the greatest known prime to number in question divided by two
            for p in myxrange(PRIMES[-1]+1,number/2):
                mod = number % p
                if mod == 0:
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
    for n in myxrange(2,number):
        mod = number % n
        if mod == 0  and isPrime(n):
            PRIME_FACTORS.append(n)
            new_number = number/n
            if isPrime(new_number):
                PRIME_FACTORS.append(new_number)
            else:
                recursive_factors(new_number)
            break
      
    
            

        
def main():
        number = 600851475143
        print number
        recursive_factors(number)
                
        PRIME_FACTORS.reverse()
        print PRIME_FACTORS[0]
        

main()
