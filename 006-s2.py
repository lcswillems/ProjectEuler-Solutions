numbers = list(range(1, 101))

square_sum = sum(numbers)**2
sum_square = sum(map(lambda i: i**2, numbers))

result = square_sum - sum_square
print(result)