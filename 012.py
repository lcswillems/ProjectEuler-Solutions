import functions

triangle = 3
i = 2
nb_divisors = 0

while nb_divisors < 500:
	i += 1
	triangle += i
	nb_divisors = len(functions.divisors(triangle, True))

print(triangle)