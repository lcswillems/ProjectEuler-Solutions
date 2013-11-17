import itertools

permut = list(itertools.permutations("0123456789"))[999999]
resultat = ''.join(permut)

print(resultat)
