import functions

divisors = sorted(functions.divisors(600851475143), reverse = True)

for divisor in divisors:
	if functions.is_prime(divisor):
		print(divisor)
		break