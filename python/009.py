target = 1000

for c in range(1,1000):
    for b in range(c):
        for a in range(b):
            if((a * a) + (b * b)) == (c * c):
                if(a + b + c) == target:
                    print(a*b*c)
            
