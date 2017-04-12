# I use the following assertion:
# 	- if m = p1^a1 * ... * pK^aK and n = p1^b1 * ... * pK^bK,
#	  gcd(m, n) = p1^(max(a1, b1)) * ... * pK^(max(aK, bK))
# 	  where p1, ..., pK be the K first prime numbers

print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)