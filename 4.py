resultat = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        produit = i*j
        if str(produit) == str(produit)[::-1]:
            if produit > resultat:
                resultat = produit

print(resultat)
