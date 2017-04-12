import functions

def is_truncatable(nb):
    nb = str(nb)
    for i in range(1, len(nb)):
        if functions.is_prime(int(nb[i:])) == False:
            return False
        if functions.is_prime(int(nb[:i])) == False:
            return False
    return True

result = 0

primes = functions.primes_below(1000000)
i = 0
j = 0

while j < 11:
    prime = primes[i]
    if prime > 10 and is_truncatable(prime):
        result += prime
        j += 1
    i += 1    

print(result)