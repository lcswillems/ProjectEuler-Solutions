import functions

result = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i*j
        if functions.is_palindrome(product) and product > result:
                result = product

print(result)
