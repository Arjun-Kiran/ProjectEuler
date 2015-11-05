
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# URL: projecteuler.net/problem=4
# Username: Arjun.Kiran

def isPalindrome(number):
    pal = str(number)
    pal = list(pal)
    pal.reverse()
    pal = ''.join(pal)
    if int(pal) == number:
        bReturn = True
    else:
        bReturn = False
        
    return bReturn


def main():
    palindrome = []
    for x in xrange(999,99,-1):
        for y in xrange(999,99,-1):
            possible_pal = x*y
            if isPalindrome(possible_pal):
                palindrome.append(possible_pal)
    
    palindrome.sort()
    palindrome.reverse()
    return palindrome[0]
                


print main()



