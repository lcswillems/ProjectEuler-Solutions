import math

def is_pandigital(nb):
    digits = []
    for i in range(1, len(str(nb))+1):
        digits.append(i)
    for i in str(nb):
        if (int(i) in digits) == True:
            digits.remove(int(i))
        else:
            return False
    return True

def is_prime(nb):
    if nb == 1:
        return False
    if nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def is_perfect(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            sum += i
    if sum == n:
        return True
    return False

def is_abundant(n):
    if sum(divisors(n)) == n:
        return True
    return False

def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors
