def isPrime(number):
    n = 2
    test_to = int(number ** .5)
    while (n <= test_to):
        if (number % n) == 0:
            return False
        else:
            n += 1
    return True

result = 0

for n in range(3,2000000,2):
    if isPrime(n) == True:
        result += n

result += 2
print(result)
