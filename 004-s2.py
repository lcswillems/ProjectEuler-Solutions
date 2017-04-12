def has_2factors_3digits(nb):
	for d in range(int(nb**0.5), 99, -1):
		q, r = divmod(nb, d)
		if r == 0 and q >= 100:
			return q < 1000
	return False

palindrome = 999999
i = 1

while palindrome > 10000:
	if has_2factors_3digits(palindrome):
		print(palindrome)
		break
	
	if i%10 == 0:
		palindrome -= 110
	else:
		palindrome -= 1100
	i += 1