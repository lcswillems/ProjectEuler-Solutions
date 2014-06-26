import functions

abundants = [i for i in range(2, 28124) if functions.is_abundant(i)]

numbers = {}

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        ssum = abundants[i] + abundants[j]
        if ssum > 28123:
            break
        numbers[ssum] = 1

result = (28123*28124)//2 - sum(numbers.keys())
        
print(result)
