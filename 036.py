import functions

result = 0

for i in range(1000000):
    if functions.is_palindrome(i):
        if functions.is_palindrome(bin(i)[2:]):
            result += i

print(result)