import functions

resultat = 2
divisors = []

for i in range(3, 2000000, 2):    
    if functions.is_prime(i):
        resultat += i

print(resultat)
