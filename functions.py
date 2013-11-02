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
    if nb == 1:
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
    sum = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            sum += i
    if sum == n:
        return True
    return False

def is_abundant(n):
    if sum(divisors(n))+1 > n:
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
    if end < 2: return []

    lng = ((end//2)-1+end%2)  
    sieve = [True]*(lng+1)  

    for i in range(int(end**0.5) >> 1):  
        if not sieve[i]: continue
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):  
            sieve[j] = False  

    primes = [2]
    
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])  

    return primes
