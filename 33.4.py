s = []
for x in range(1,100):
    sum = 0
    for y in range(1,x):
        if x % y == 0:
            sum += y
    if sum == x:
        s.append(x)
print(s)