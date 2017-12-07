# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# Project Euler Problem 10
# NOT SOLVED: because it has a long execution time.  
import math, sys, os


class PrimeFinder:
    def __init__(self):
        self.aPrime = [2]
        self.sum = 2

    def addPrime(self,nPrime):
        self.aPrime.append(nPrime)
        self.aPrime.sort()
        
    def fermatLittle(self,nNumber):
        prime = False
        for i in xrange(2,nNumber):
            a = (i**nNumber) % nNumber 
            b = i%nNumber
            if a == b:
                prime = True
                break
            else:
                prime = False
                break
                
        return prime

    def isPrime(self,nNumber):
        prime = True
        if self.fermatLittle(nNumber):
            prime = True
            # for number in self.aPrime:
                    # if (nNumber%number) == 0:
                        # prime = False
                        # break
        else:
            prime = False
            
        return prime

    def primeRange(self,nRange):
        for i in xrange(2,nRange):
            #if self.isPrime(i) and i not in self.aPrime:
            if self.isPrime(i):
                #self.addPrime(i)
                self.sum += i

    def sumPrimeArray(self):
        sum = 0
        for i in self.aPrime:
            sum += i 
        return sum

    def solution(self,nRange):
        self.primeRange(nRange)
        #print self.aPrime
        return self.sum

if __name__ == '__main__':
    sumPrime = PrimeFinder()
    #print sumPrime.solution(10)
    print sumPrime.solution(2000000)

        
