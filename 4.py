import functions

resultat = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        produit = i*j
        if functions.is_palindrome(produit):
            if produit > resultat:
                resultat = produit

print(resultat)
