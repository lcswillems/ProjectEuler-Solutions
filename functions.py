import math
import fractions

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
    if nb < 2:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

def is_perfect(n):
    return sum(divisors(n))+1 == n

def is_abundant(n):
    return sum(divisors(n))+1 > n

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

def max_path_sum(triangle):
    triangle = list(reversed([[int(j) for j in i.split()] for i in triangle.split("\n")]))
    for i in range(1, len(triangle)):
        for j, k in enumerate(triangle[i]):
            triangle[i][j] = k + max([triangle[i-1][j], triangle[i-1][j+1]])

    return triangle[-1][0]

def is_palindrome(nb):
    if str(nb) == str(nb)[::-1]:
        return True
    return False

def distinct_prime_factors(nb):
    factors = []
    gcd = 0
    
    for i in range(2, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(q):
                factors.append(q)

    return list(set(factors))

def primes_below(end):
    if end < 2:
        return []

    lng = (end//2) - 1
    primes = [True]*lng  

    for i in range(int(lng**0.5)):  
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  

    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

def is_permutation_of(nb1, nb2):
    nb1, nb2 = list(str(nb1)), list(str(nb2))

    for i in nb1:
        if i in nb2:
            nb2.remove(i)
        else:
            return False

    return True
