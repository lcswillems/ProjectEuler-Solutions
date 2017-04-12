import math
import fractions

# This function checks if the number "nb" is pandigital.
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

# This function checks if the number "nb" is prime.
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

# This function checks if the number "nb" is perfect.
def is_perfect(nb):
	return sum(divisors(nb))+1 == nb

# This function checks if the number "nb" is abundant.
def is_abundant(nb):
	return sum(divisors(nb))+1 > nb

# This function checks if the number "nb" is a palindrome.
def is_palindrome(nb):
	if str(nb) == str(nb)[::-1]:
		return True
	return False

# This function checks if the string "s1" is an anagram
# of the string "s2".
def is_anagram(s1, s2):
	if len(s1) != len(s2):
		return False

	s1, s2 = list(s1), list(s2)

	while len(s1) > 0:
		try:
			e = s1.pop()
			s2.remove(e)
		except:
			return False

	return True

# This function returns the list of the divisors of the
# number "nb". If "extremum" is True, 1 and "nb" are included.
def divisors(nb, extremum = False):
	divisors = []
	inf = 1 if extremum else 2
	
	for i in range(inf, int(nb**0.5)+1):
		q, r = divmod(nb, i)
		if r == 0:
			if q >= i:
				divisors.append(i)
				if q > i:
					divisors.append(q)

	return divisors

# This function returns the list of the distinct prime
# factors of the number "nb".
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

# This function returns the list of primes below
# the number "end". It uses the sieve of Eratosthenes.
def primes_below(end):
	if end < 2:
		return []

	middle = (end//2) - 1
	primes = [True]*middle  

	for i in range(int(middle**0.5)):  
		if primes[i]:
			for j in range(2*i*(i + 3) + 3, middle, 2*i + 3):
				primes[j] = False  

	return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

# This function returns the product of the numbers
# in the list "nbs".
def product(nbs):
	prod = 1
	for i in nbs:
		prod *= int(i)
	return prod

# This function returns the prime decomposition of the
# number "nb".
def prime_decomposition(nb):
	decompo = {}
	i = 2
	j = 0
	while i <= nb or j > 0:
		q, r = divmod(nb, i)
		if r == 0:
			nb = q
			j += 1
		else:
			if j > 0:
				decompo[i] = j
			i += 1
			j = 0
	return decompo

# This function returns x**y % z but using the exponentiation
# by squaring.
def pow_mod(x, y, z):
	number = 1
	while y:
		if y & 1:
			number = number * x % z
		y >>= 1
		x = x * x % z
	return number