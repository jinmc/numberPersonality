def main():
    "This is the main loop, which iterates from 1 to limit."
    limit = 100
    for a in range(1, limit + 1):
        print(a,'\t', end = '');
        if is_prime(a):
            print('prime, ', end = '')
        else:
            print('composite, ', end = '')
        if is_happy(a):
            print('happy, ', end = '')
        else:
            print('unhappy, ', end = '') 

        if is_triangular(a):
            print('triangular, ', end = '')
        else:
            print('not triangular, ', end = '')
        if is_square(a):
            print('square, ', end = '')
        else:
            print('not square, ', end = '')
        if is_smug(a):
            print('smug, ', end = '')
        else:
            print('not smug, ', end = '')
        if is_honest(a):
            print('honest')
        else:
            print('dishonest')



def is_prime(n):
    """determines prime or composite"""
    if n <= 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for m in range (2, n): # We only have to check until n/2      
        if n % m == 0:
            return False
    return True

def is_happy(n):
    """If we can divide the numbers to strings and square it and the sum becomes 1,
    we're happy. If not, we're unhappy."""
    if n <= 0:
        return False
    while n != 1 and n != 4:
        k = 0
        Sum = 0
        while n >= 10 ** k:
            k += 1
        k -= 1                     # Shows how much tens of power degree is n
        while k >= 0:              # Actually doing calculation
            Sum += ( n // (10 ** k)) ** 2
            n -= ( n // (10 ** k)) * (10 ** k)
            k -= 1

        n = Sum                    # returning back Sum to n
    if n == 4:                     #infinite loop
        return False
    elif n == 1:
        return True
    
def is_triangular(n):
    """Can this number be expressed as 1 + 2 + ... + k ? """
    if n <= 0:
        return False
    for m in range (1, n + 1):
        if n == m * (m + 1) / 2:
            return True
    return False
            
def is_square(n):
    """1+3+5+...2k+1"""
    if n <= 0:
        return False
    for m in range (1, n + 1):
        if n == m ** 2:    
            return True
    return False       

def is_smug(n):
    """If n is the sum of two squares, it is smug. Else, it is not smug."""
    if n <= 0:
        return False    
    for a in range (1, n):
        for b in range (1, n):
            if n == a ** 2 + b ** 2:
                return True
    return False      
    
def is_honest(n):
    """The number is dishonest if n // k = k but n is not n = k^2"""
    if n <= 0:
        return False
    for k in range (1, n):
        if n / k == k:
            return True
        elif n // k == k:
            return False
    return True


if __name__ == "__main__":
    main()
