import functions

limit = 28123

abundants = [i for i in range(2, limit+1) if functions.is_abundant(i)]
abundant_sums = set()

for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		abundant_sum = abundants[i] + abundants[j]
		if abundant_sum > limit:
			break
		abundant_sums.add(abundant_sum)

result = limit*(limit+1)//2 - sum(list(abundant_sums))
print(result)