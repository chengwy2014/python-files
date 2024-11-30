# # # # # # # # 因为IDLE很难用，所以不用IDLE
# # # # # # # i_d = []
# # # # # # # for i in range(10,100):
# # # # # # #     i_a = str(i[0])
# # # # # # #     i_b = str(i[1])
# # # # # # #     i_a = int(i_a)
# # # # # # #     i_b = int(i_b)
# # # # # # #     i_c = (i_a + i_b) + (i_a * i_b)
# # # # # # #     if i_c == i:
# # # # # # #         i_d.append(i)
# # # # # # # print(i)
# # # # # # a = 0
# # # # # # b = 0
# # # # # # for i in range(10,100):
# # # # # #     c = str(i)
# # # # # #     a = int(c[0])
# # # # # #     b = int(c[1])
# # # # # #     if i == (a + b) + (a * b):
# # # # # #         print(i)
# # # # # a = 0
# # # # # b = 0
# # # # # d = []
# # # # # for i in range(10,100):
# # # # #     c = str(i)
# # # # #     a = int(c[0])
# # # # #     b = int(c[1])
# # # # #     if i == (a + b) + (a * b):
# # # # #         d.append(i)
# # # # # print(d)
# # # # for i in range(1000,10000):
# # # #     a = str(i)
# # # #     b = a[0]
# # # #     c = a[1]
# # # #     d = a[2]
# # # #     e = a[3]
# # # #     f = b + d + e
# # # #     g = int(f)
# # # #     if c == "0":
# # # #         if i == g * 9:
# # # #             print(i)
# # # h = []
# # # for i in range(1000,10000):
# # #     a = str(i)
# # #     b = a[0]
# # #     c = a[1]
# # #     d = a[2]
# # #     e = a[3]
# # #     f = b + d + e
# # #     g = int(f)
# # #     if c == "0":
# # #         if i == g * 9:
# # #             h.append(i)
# # # print(h)
# # lst = []
# # for i in range(100,1000):
# #     i_str = str(i)
# #     i_a = int(i_str[0])
# #     i_b = int(i_str[1])
# #     i_c = int(i_str[2])
# #     i_a_ = i_a ** 3
# #     i_b_ = i_b ** 3
# #     i_c_ = i_c ** 3
# #     if i_a_ + i_b_ + i_c_ == i:
# #         lst.append(i)
# # print(lst)
# for x in range(100,1000):
#     n = str(x)
#     sum = 0
#     for y in n:
#         sum += int(y) ** 3
#     if x == sum:
#         print(x)
lst = []
i_a = 0
i_b = 0
i_c = 0
i_d = 0
for i in range(1000,10000):
    _i = str(i)
    i_a = _i[0]
    i_b = _i[1]
    i_c = _i[2]
    i_d = _i[3]
    i_a = int(i_a)
    i_b = int(i_b)
    i_c = int(i_c)
    i_d = int(i_d)
    i_a = i_a ** 4
    i_b = i_b ** 4
    i_c = i_c ** 4
    i_d = i_d ** 4
    if i_a + i_b + i_c + i_d == i:
        print(i)