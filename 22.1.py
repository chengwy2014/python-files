# # # # # # import random
# # # # # # sum = 0
# # # # # # m = []
# # # # # # for x in range(10):
# # # # # #     m.append(random.randint(1,20))
# # # # # # num = m[0]
# # # # # # for x in range (10):
# # # # # #     if m[x] < num:
# # # # # #         num = m[x]
# # # # # #     sum += m[x]
# # # # # # print(num)
# # # # # # print(sum)
# # # # # import random
# # # # # sum = 0
# # # # # m = []
# # # # # for x in range(10):
# # # # #     m.append(random.randint(1,20))
# # # # # num = m[0]
# # # # # for x in range (10):
# # # # #     if m[x] > num:
# # # # #         num = m[x]
# # # # #     sum += m[x]
# # # # # print(num)
# # # # # print(sum/10)
# # # # for x in range(1,10):
# # # #     line = ""
# # # #     for y in range(1,x + 1):
# # # #         i = str(x)
# # # #         j = str(y)
# # # #         r = str(x*y)
# # # #         row = j + "*" + i + "=" + r + " "
# # # #         line += row
# # # #     print(line)
# # # import random
# # # num = []
# # # a = 0
# # # for rand in range(10):
# # #     a = random.randint(1,100)
# # #     num.append(a)
# # # print(num)
# # # for x in range(10 - 1):
# # #     for y in range(9 - x):
# # #         if num[y] < num[y + 1]:
# # #             num[y],num[y + 1] = num[y + 1],num[y]
# # # print(num)
# # from random import randint
# # m = []
# # for x in range(5):
# #     n = randint(1,100)
# #     m.append(n)
# # print(m)
# # for x in range(4):
# #     for y in range(x + 1,5):
# #         if m[x] > m[y]:
# #             m[x],m[y] = m[y],m[x]
# # print(m)
# n = input("请输入4位数值：")
# n = int(n)
# print(n // 1000)
# n = n % 1000
# print(n // 100)
# n = n % 100
# print(n // 10)
# n = n % 10
# print(n // 1)
for i in range(1000,10000):
    