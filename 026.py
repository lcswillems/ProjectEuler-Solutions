def cycle_length(den):
    remainder = 10
    i = 0

    while remainder != 10 or i < 1:
        remainder = (remainder % den) * 10
        i += 1

    return i

longest = 0

for i in range(2, 1000):
    if i%2 != 0 and i%5 != 0:
        length = cycle_length(i)
        if length > longest:
            longest = length
            result = i

print(result)
