import math

def sum_of_digit_fact(n):
	s = 0

	while n != 0:
		n, r = divmod(n, 10)
		s += math.factorial(r)

	return s

result = 0

for i in range(3, 1000000):
    if i == sum_of_digit_fact(i):
        result += i

print(result)