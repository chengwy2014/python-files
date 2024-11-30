# # # # # from random import randint
# # # # # numbers = []
# # # # # for a1 in range(5):
# # # # #     rand_int = randint(1,100)
# # # # #     numbers.append(rand_int)
# # # # # print("old list(The random numbers)" + str(numbers))
# # # # # for a2 in range(4):
# # # # #     for a3 in range(a2 + 1,5):
# # # # #         if numbers[a2] > numbers[a3]:
# # # # #             numbers[a2],numbers[a3]=numbers[a3],numbers[a2]
# # # #
# # # # b1 = input("Year = ")
# # # # b2 = int(b1)
# # # #
# # # # b3 = b2 // 1000
# # # # b4 = b2 % 1000
# # # #
# # # # b5 = b4 // 100
# # # # b6 = b2 % 100
# # # #
# # # # b7 = b6 // 10
# # # # b8 = b4 % 10
# # # #
# # # # b9 = b8 // 1
# # # # b10 = b6 % 1
# # # #
# # # # print("Year numbers:" + str(b3) + "," + str(b5) + "," + str(b7) + "," + str(b9))
# # # for x in range(1000,10000):
# # #     n = x
# # #     a = x // 1000
# # #     n = n % 1000
# # #     b = n // 100
# # #     n = n % 100
# # #     c = n // 10
# # #     n = n % 10
# # #     d = n // 1
# # #     if a + b + c + d == 35:
# # #         print(x)
# #
# #
# # from math import pow
# # n = 2018
# # for x in range(4):
# #     m = pow(10,3 - x)
# #     print(n//m)
# #     n = n % m
#
#
# n = 2018
# s = str(n)
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])


for x in range(400,499):
    n = str(x)
    a = n[0]
    b = n[2]
    if int(b) > int(a):
        print(x)