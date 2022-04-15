# Prime Factorization Work
'''
number = 24
primes = []
factors = []

while number != 1:
    for n in range(2, int(number)+1):
        if number % n == 0:
            print("{} is divisible by {}".format(number, n))
            number = number / n
            factors.append(n)
            break

print(factors)
product = 1

for n in range(0,len(factors)):
    product = product * factors[n]

print(product)

'''

number = 38
check = False

while check == False:
    for n in range(2,21):
        if number % n != 0:
            number += 38
            break
        elif n == 20:
            check = True

print(number)
