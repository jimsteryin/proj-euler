_number = 600851475143

def isPrime(number):
    n = 2
    test_to = int(number ** .5)
    while (n < test_to):
        if (number % n) == 0:
            return False
        else:
            n += 1
    return True

def factorPair(fac1):
    return _number / fac1

factor1 = 0
factor2 = 0
count = 2

while _number % count != 0:
    count += 1

factor1 = count
factor2 = factorPair(factor1)

print(factor2)
print(isPrime(factor2))

count += 1

while(isPrime(factor2)) == False:
    while _number % count != 0:
        count += 1
    factor1 = count
    factor2 = factorPair(factor1)
    count += 1

print(factor2)
