a = 1
b = 1

result = 2

while len(str(b)) < 1000:
    a, b = b, a+b
    result += 1

print(result)
