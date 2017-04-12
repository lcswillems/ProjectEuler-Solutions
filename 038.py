import functions

result = 0

for i in range(1, 100000):
    products = ""
    for n in range(1, 9):
        products += str(n * i)
        if len(products) == 9:
            if functions.is_pandigital(products):
                if int(products) > result:
                    result = int(products)
        elif len(products) > 9:
            break
        
print(result)