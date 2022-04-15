def search(test, num_list):
    for i in range(len(num_list)):
        if num_list[i] == test:
            return True
        
    return False


numbers = []
result = 1

for a in range(2,101):
    for b in range(2,101):
        result = a ** b
        if search(result, numbers) == False:
            numbers.append(result)

print(len(numbers))
