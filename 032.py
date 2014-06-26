import functions

result = 0
products = []

for i in range(1, 10000):
    for j in range(i, 10000):
        product = i*j
        concat = str(i)+str(j)+str(product)
        if len(concat) == 9:
            if functions.is_pandigital(concat):
                products.append(product)
        elif len(concat) > 9:
            break

print(sum(set(products)))
