import functions

nb_primes = 1
i = 1

while nb_primes != 10001:
	i += 2
	if functions.is_prime(i):
		nb_primes += 1

print(i)