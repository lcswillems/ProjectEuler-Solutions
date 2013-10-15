import functions

divisors = functions.divisors(600851475143)
divisors.sort(reverse=True)

for i in divisors:
    if functions.prime(i):
        print(i)
        break
