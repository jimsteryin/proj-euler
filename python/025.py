fib1 = 1
fib2 = 1
fibn = 0

def fib(num1, num2):
    return num1 + num2

fibn = fib(fib1, fib2)
count = 2
'''
while (fibn / 10) <= 1:
    fibn = fib(fib1, fib2)
    fib1 = fib2
    fib2 = fibn
    count += 1
#    print(fibn)

print("Get to 2 digits: ",count)

while (fibn / 100) <= 1:
    fibn = fib(fib1, fib2)
    fib1 = fib2
    fib2 = fibn
    count += 1
#    print(fibn)

print("Get to 3 digits: ",count)

while (fibn / 1000) <= 1:
    fibn = fib(fib1, fib2)
    fib1 = fib2
    fib2 = fibn
    count += 1
#    print(fibn)

print("Get to 4 digits: ",count)

while (fibn / 10000) <= 1:
    fibn = fib(fib1, fib2)
    fib1 = fib2
    fib2 = fibn
    count += 1
#    print(fibn)

print("Get to 5 digits: ",count)
'''

for i in range(1,1000):
    while (fibn / (10 ** i)) <= 1:
         fibn = fib(fib1, fib2)
         fib1 = fib2
         fib2 = fibn
         count += 1
    #print("Get to {} digits: {}".format((i+1),count))
print(count)

'''
fibncc = [1, 1]
while len(str(fibncc[-1]))<1000: fibncc.append(fibncc[-1]+fibncc[-2])

print(len(fibncc), '\n')
'''
