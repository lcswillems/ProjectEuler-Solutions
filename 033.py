def is_canceled_fraction(num, den):
    num = str(num)
    den = str(den)
    
    if "0" in num+den or (not(num[0] in den) and not(num[1] in den)):
        return False

    place = 0 if num[0] in den else 1
    num_new = num[1-place]
    den_new = den.replace(num[place], '', 1)

    return int(num_new)/int(den_new) == int(num)/int(den)

import fractions

product = 1

for den in range(11, 100):
    for num in range(11, den):
        if is_canceled_fraction(num, den):
            product *= fractions.Fraction(num, den)

print(product.denominator)
