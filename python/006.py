sumsquare = 0
squaresum = 0

for n in range(1,101):
    sumsquare += n * n
    squaresum += n

print((squaresum * squaresum) - sumsquare)
