# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



def isPrime(number):
    bReturn = True
    for n in xrange(2,number):
        mod = number % n
        if mod == 0 and n != number:
            bReturn = False
            break
    
    return bReturn

def factors(number):
    primeFactors = []
    for n in xrange(2,number+1):
        mod = number % n
        if mod == 0  and isPrime(n):
            primeFactors.append(n)
            new_number = number/n
            
            if isPrime(new_number):
                primeFactors.append(new_number)
            else:
                primeFactors.extend(factors(new_number))
            break
            
    return primeFactors
    
    
def main():
    factorList = []
    for n in xrange(2,20 + 1):
        fac = factors(n)
        for f in fac:
            if f in factorList:
                if fac.count(f) > factorList.count(f):
                    factorList.append(f)
            else:
                factorList.append(f)
                
    product = 1
    for n in factorList:
        product = product*n
    
    return product
    
print main()
        
