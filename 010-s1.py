import functions

result = 2

for i in range(3, 2000000, 2):    
	if functions.is_prime(i):
		result += i

print(result)