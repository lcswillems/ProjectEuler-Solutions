import functions

def is_circular(nb):
	nb = str(nb)
	
	if len(nb) == 1:
		return True

	for i in nb:
		if i in "02468":
			return False
	
	for i in range(len(nb)):
		nb = nb[1:] + nb[0]
		if functions.is_prime(int(nb)) == False:
			return False

	return True

primes = functions.primes_below(1000000)
result = 0

for prime in primes:
	if is_circular(prime):
		result += 1

print(result)