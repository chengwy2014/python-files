# # p = []
# # for i in range(10,100):
# #     i = str(i)
# #     i1 = i[0]
# #     i2 = i[1]
# #     if int(i) == ( int(i1) + int(i2) ) + ( int(i1) * int(i2) ):
# #         p.append(i)
# #     else:
# #         continue
# # print(p)
#
# for x in range(1,10):
#     for y in range(100):
#         a = str(x)
#         b = str(y).zfill(2)
#         n = a + '0' + b
#         m = a + b
#         if int(n) == int(m)*9:
#             print(n)

for x in range(100,1000):
    n = str(x)
    sum = 0
    for y in n:
        sum += int(y)**3
    if x == sum:
        print(x)