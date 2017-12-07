
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# URL: projecteuler.net/problem=4
# Username: Arjun.Kiran

def reverseNumber(number):
    """Reverses number"""
    pal = str(number)
    pal = list(pal)
    pal.reverse()
    pal = ''.join(pal)
    return int(pal)    


def isPalindrome(number):
    """ checks if palindrome """
    pal = reverseNumber(number)
    if pal == number:
        bReturn = True
    else:
        bReturn = False
        
    return bReturn

def whoIsLargest(possible, current):
    if(current > possible):
        return current
    else:
        return possible

def main():
    palindrome = 0
    # range from 999 to 100 in reverse order
    for x in xrange(999,99,-1):
        for y in xrange(999,99,-1):
            possible_pal = x*y
            if isPalindrome(possible_pal):
                palindrome = whoIsLargest(possible_pal,palindrome)
    
    return palindrome            

if __name__ == '__main__':
    print main()




