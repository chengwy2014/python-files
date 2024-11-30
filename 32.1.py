# s = []
# for i in range(10,100):
#     a = i // 10
#     b = i % 10
#     n = a * b
#     if n > 1:
#         flag = True
#         for y in range(2,n):
#             if n % y == 0:
#                 flag = False
#                 break
#         if flag:
#             s.append(i)
# print(s)
s = []
m = []
for x in range(2,100):
    flag = True
    n = 2
    while n < x:
        if x % n == 0:
            flag = False
            break
        else:
            n += 1
    if flag:
        s.append(x)
print(s)
for i in range(4,100):
    if i % 2 == 0:
        m.append(i)
print(m)
for i in m:
    for j in s:
        a = j
        b = i - j
        if b in s:
            print(str(i) + '=' + str(a) + '+' + str(b))
            break