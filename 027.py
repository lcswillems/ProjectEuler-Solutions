import functions

# We remark that:
#	- for n = 0, n² + an + b = b so 'b' should be a prime.
#	- for n = 1, n² + an + b = (a+1) + b should be a prime
#     so 'a' should be odd.

primes = functions.primes_below(1000)
max_n = 0

for b in primes:
    for a in range(-999, 1000, 2):
        f_n = b
        n = 0

        while functions.is_prime(f_n):
            n += 1
            f_n = n**2 + a*n + b
        
        if n > max_n:
            max_n = n
            result = a*b

print(result)