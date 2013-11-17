import functions

primes = functions.primes_below(1000)
longest = 0

for b in primes:
    for a in range(-999, 1000, 2):
        image = b
        n = 0

        while functions.is_prime(image):
            n += 1
            image = n**2 + a*n + b
        
        if n > longest:
            longest = n
            resultat = a*b

print(resultat)
