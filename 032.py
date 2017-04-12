import functions

result = 0

for i in range(1, 10000):
    for j in range(i, 10000):
        product = i*j
        concat = str(i)+str(j)+str(product)
        if len(concat) > 9:
        	break
       	if len(concat) == 9 and functions.is_pandigital(concat):
            result += product

print(result)