# We want to compute (Σ i)² - Σ (i²).
# As Σ i = n(n+1)/2 and Σ (i²) = n(n+1)(2n+1)/6,
# (Σ i)² - Σ (i²) = n(n+1)(3n²-n-2)/12.

n = 100

result = n*(n+1)*(3*n**2-n-2)//12
print(result)