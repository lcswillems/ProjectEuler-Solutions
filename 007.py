import functions

nb_prime = 1
i = 1

while nb_prime != 10001:
    i += 2
    if functions.is_prime(i):
        nb_prime += 1

print(i)
