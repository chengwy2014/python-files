m = input('m:')
n = input('n:')
m = int(m)
n = int(n)
temp = m
while True:
    if m % temp == 0 and n % temp == 0:
        break
    else:
        temp -= 1
print("最大公因数为：",temp)