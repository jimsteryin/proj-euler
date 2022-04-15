import math

large = 2 ** 1000
sum = 0
'''
while large > 0:
    sum += (large % 10)
    large = large - (large % 10)
    large = int(large/10)

print(sum)
'''

largenum = str(large)

for n in range(0,len(largenum)):
    sum += int(largenum[n])

print(large)
print(largenum)
print(len(largenum))
print(sum)
