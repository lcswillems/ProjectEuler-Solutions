def has_2factors_3digits(nb):
    for i in range(int(nb**0.5)+1, 99, -1):
        q, r = divmod(nb, i)
        if r == 0:
            if len(str(q)) == 3:
                return True
            elif len(str(q)) > 3:
                return False
    return False

i = 997799
j = 1

while i > 10000:
    if has_2factors_3digits(i):
        print(i)
        break
    
    if j%10 == 8:
        i -= 110
    else:
        i -= 1100
    j += 1
