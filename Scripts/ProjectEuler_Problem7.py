import math
# Borrowed algorithm from my Project Euler Problem 3
PRIMES = [2]
 
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
            for p in xrange(PRIMES[-1]+1,number/2):
                mod = number % p
                if mod == 0:
                    bReturn = False
                    break
                    
            if bReturn == True:
                PRIMES.append(number)
                
    return bReturn 
    
    
def main(numberPrimes):
    global PRIMES
    n = 1
    while(len(PRIMES) < numberPrimes):
        n = n + 1
        isPrime(n)
        
    return PRIMES[-1]
    

print main(10001)
        