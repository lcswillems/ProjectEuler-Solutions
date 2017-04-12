result = 1

dim = 1001
n = 1

for k in range(2, dim, 2):
    for j in range(4):
        n += k
        result += n

print(result)