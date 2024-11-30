# # # # # for i in range(100,1000):
# # # # #     i_1 = str(i)[0]
# # # # #     i_2 = str(i)[1]
# # # # #     i_3 = str(i)[2]
# # # # #     if i == int(i_1) ** 3 + int(i_2) ** 3 + int(i_3) ** 3:
# # # # #         print(i)
# # # # #     else:
# # # # #         continue
# # # # for i in range(1000,10000):
# # # #     i_1 = str(i)[0]
# # # #     i_2 = str(i)[1]
# # # #     i_3 = str(i)[2]
# # # #     i_4 = str(i)[3]
# # # #     if i == int(i_1) ** 4 + int(i_2) ** 4 + int(i_3) ** 4 + int(i_4) ** 4:
# # # #         print(i)
# # # #     else:
# # # #         continue
# # # a = 0
# # # for i in range(1986,2021,4):
# # #     a += 1
# # # print(a)
# # n = 0
# # x = 0
# # while x != 100:
# #     n += 9 + 2 * x
# #     x += 1
# # print(n)
# es = []
# os = []
# a = 0
# b = 1
# for x in range(20):
#     a,b=b,a+b
#     if a%2 == 0:
#         es.append(a)
#     else:
#         os.append(a)
# print(a)
# print(len(es))
# print(len(os))
# print(os[9])
s = []
for x in range(6,101):
    if x % 6 == 0:
        s.append(x)
    print(s)