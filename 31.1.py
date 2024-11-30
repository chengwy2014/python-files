# # # s = []
# # # for x in range(2,100):
# # #     flag = True
# # #     n = 2
# # #     while n < x:
# # #         if x % n == 0:
# # #             flag = False
# # #             break
# # #         else:
# # #             n += 1
# # #     if flag:
# # #         s.append(x)
# # # print(s)
# # n = input("请输入要判断的数：")
# # n = int(n)
# # flag = True
# # for x in range(2,n):
# #     if n % x == 0:
# #         flag = False
# #         break
# # if flag:
# #     print("YES")
# # else:
# #     print("NO")
# import asyncio.sslproto
# s = []
# for x in range(10,100):
#     a = x // 10
#     b = x % 10
#     n = a * b
#     if n > 1:
#         flag = True
#         for y in range(2,n):
#             if n % y == 0:
#                 flag = False
#                 break
#         if flag:
#             s.append(x)
# print(s)
s = []
for x in range(2,100):
    flag = True
    for y in range(2,x):
        if x % y == 0:
            flag = False
            break
    if flag:
        s.append(x)
print("质数列表：",s)
m = []
for x in range(4,100):
    if x % 2 == 0:
        m.append(x)
print("偶数列表：",m)
for x in m:
    for y in s:
        a = y
        b = x - y
        if b in s:
            print(str(x) + '=' + str(a) + '+' + str(b))
        break