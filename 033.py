def is_canceled_fraction(num, den):
    num = str(num)
    den = str(den)

    if "0" in num+den or not(num[0] in den or num[1] in den):
        return False

    pos = 0 if num[0] in den else 1
    new_num = num[1-pos]
    new_den = den.replace(num[pos], '', 1)

    return int(new_num)/int(new_den) == int(num)/int(den)

import fractions

product = 1

for den in range(11, 100):
    for num in range(11, den):
        if is_canceled_fraction(num, den):
            product *= fractions.Fraction(num, den)

print(product.denominator)
