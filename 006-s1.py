sum_squares = 0
square_sum = 0

for i in range(1, 101):
	sum_square += i**2
	square_sum += i

square_sum = square_sum ** 2

result = square_sum ** 2 - sum_square
print(result)