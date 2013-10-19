import math

def pandigital(nb):
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
    for i in range(2, int(math.sqrt(nb)) + 1):
        if nb%i == 0:
            return False
    return True

def perfect(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            sum += i
    if sum == n:
        return True
    return False

def abundant(n):
    if sum(divisors(n)) == n:
                return True
    return False

def factorial(nb):
    for i in range(2, nb):
        nb *= i
    return nb

def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    
    for i in range(inf, int(math.sqrt(nb)) + 1):
        if nb%i == 0:
            if nb//i > i:
                divisors.append(i)
                divisors.append(nb//i)
            elif nb//i == i:
                divisors.append(i)
    return divisors
