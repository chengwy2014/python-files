m = []
for x in range(1,25):
    if 24 % x == 0 and 36 % x == 0:
        m.append(x)
print(m)
print(max(m))