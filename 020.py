import math

fact = str(math.factorial(100))

resultat = 0

for i in fact:
    resultat += int(i)

print(resultat)
