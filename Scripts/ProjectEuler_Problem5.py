# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def isDivisible(number, div):
    return (number % div == 0)

def isPrime(number):
    """Determine if number is prime """
    bReturn = True
    for n in xrange(2,number):
        if isDivisible(number,n) and n != number:
            bReturn = False
            break
    
    return bReturn

def factors(number):
    """Finds all the factors """
    primeFactors = []
    for n in xrange(2,number+1):
        if isDivisible(number,n) and isPrime(n):
            primeFactors.append(n)
            new_number = number/n
            
            if isPrime(new_number):
                primeFactors.append(new_number)
            else:
                primeFactors.extend(factors(new_number))
            break
            
    return primeFactors

def factorCompile(lst):
    """Multipling all the numbers in the list"""
    product = 1
    for n in lst:
        product = product*n

    return product    
    
    
def main():
    factorList = []
    for n in xrange(2,20 + 1):
        # finding all the factors
        fac = factors(n)
        for f in fac:
            if f in factorList:
                # need to match the minimum factors required
                if fac.count(f) > factorList.count(f):
                    factorList.append(f)
            else:
                # new factor that is not exisiting in the factor list
                factorList.append(f)
                

    return factorCompile(factorList)

if __name__ == '__main__':
        print main()    

        
