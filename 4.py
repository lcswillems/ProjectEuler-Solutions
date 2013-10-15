resultat = 0

for i in range(100, 1000):
    for j in range(100, i):
        produit = i*j
        if str(produit)== str(produit)[::-1]:
            if produit > resultat:
                resultat = produit

print(resultat)
