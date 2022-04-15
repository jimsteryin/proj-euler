def is_palindrome(num):
    return str(num) == str(num)[::-1]

maxPal = 0

for x in range(100,1000):
    for y in range(100,1000):
        product = x * y
        if product > maxPal and is_palindrome(product):
            maxPal = product

print(maxPal)
