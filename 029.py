powers = [a**b for a in range(2, 101) for b in range(2, 101)]
result = len(list(set(powers)))
print(result)