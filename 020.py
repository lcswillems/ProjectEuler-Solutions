import math

fact = str(math.factorial(100))

result = 0

for i in fact:
    result += int(i)

print(result)
