def is_sum_fifth_powers_of_digits(nb):
    return nb == sum([int(i)**5 for i in str(nb)])

result = sum(filter(is_sum_fifth_powers_of_digits, range(2, 354295)))
print(result)