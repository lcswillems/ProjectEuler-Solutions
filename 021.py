import functions

def d(nb):
    return 1 + sum(functions.divisors(nb))

resultat = 0

for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b:
        resultat += a

print(resultat)
