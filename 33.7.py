m = input('m:')
n = input('n:')
m = int(m)
n = int(n)
while True:
    if m % n == 0:
        break
    else:
        m,n = n,m % n
print("最大公因数为：",n)