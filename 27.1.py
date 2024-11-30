# # # # s = 'python'
# # # # print(s[1:3:1])
# # # # print(s[1:3])
# # # # print(s[:3:])
# # # # print(s[1::])
# # # # print(s[::-1])
# # # for x in range(1,219):
# # #     n = str(x)
# # #     sum = 0
# # #     for y in n:
# # #         sum += int(y)
# # #     if sum % 5 == 0:
# # #         print(x)
# # nums = ['00','11','22','33','44','55','66','77','88','99']
# # for x in range(10):
# #     n = '2018' + nums[x]
# #     if int(n) % 12 == 0:
# #         print(int(n))
# import sys
#
# #设置允许最大位数，比如10000
# sys.set_int_max_str_digits(10000)
#
# s = '2008' * 2008
# n = int(s)
# print(str(n % 13))
n = 4
while True:
    s = '2009' * n + '736'
    print(s)
    if int(s) % 11 == 0:
        break
    else:
        n += 1
    print(n)