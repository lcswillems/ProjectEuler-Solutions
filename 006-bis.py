numbers = list(range(1, 101))

square_sum = sum(numbers)**2
sum_square = sum([i**2 for i in numbers])
result = square_sum - sum_square

print(result)
