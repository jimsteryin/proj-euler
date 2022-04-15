file = "C:/Users/Jimmy/OneDrive/Python/Project Euler/008.txt"

numbers = []

with open(file) as f:
    while True:
        c = f.read(1)
        if not c:
            print("End of File")
            break
        # print ("Read a character:", c)
        numbers.append(int(c))

#print(numbers)

large = 0
product = 1

for n in range(0,(len(numbers) - 13)):
    for y in range(0,13):
        product *= numbers[n+y]
    if product > large:
        large = product
    product = 1

print(large)
