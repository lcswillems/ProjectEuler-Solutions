import functions

abundants = [i for i in range(2, 28124) if functions.is_abundant(i)]

numbers = {}

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        somme = abundants[i] + abundants[j]
        if somme > 28123:
            break
        numbers[somme] = 1

resultat = (28123*28124)//2 - sum(numbers.keys())
        
print(resultat)
