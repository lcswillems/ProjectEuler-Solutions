import functions

divs = functions.divisors(600851475143)
divs.sort(reverse=True)

for i in divs:
    if functions.is_prime(i):
        print(i)
        break
