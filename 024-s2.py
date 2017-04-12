import math

def permutations(s):
	if len(s) == 1:
		return [s]

	perms = []

	for k in range(len(s)):
		perms += [s[k] + perm for perm in permutations(s[:k] + s[k+1:])]

	return perms

print(permutations("0123456789")[999999])