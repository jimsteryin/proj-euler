def fibonacci(num1, num2):
    return num1 + num2

fibn1 = 1
fibn2 = 2
fibn = fibonacci(fibn1, fibn2)
fibsum = 0

while fibn < 4000000:
    fibn = fibonacci(fibn1,fibn2)
    fibn1 = fibn2
    fibn2 = fibn
    if fibn % 2 == 0:
        fibsum += fibn

print (fibsum + 2)
