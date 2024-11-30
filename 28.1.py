# # import sys
# # sys.set_int_max_str_digits(10000)
# # s = ""
# # for x in range(1,104,2):
# #     n = str(x)
# #     s += n
# # print(len(s))
# # print(int(s) % 9)
# import sys
# sys.set_int_max_str_digits(10000)
# x = 9
# n = 0
# for i in range(100):
#     n += x
#     n += 2
# print(n)
import sys

sys.set_int_max_str_digits(10000)
a = 0
b = 1
oushu = []
jishu = []

for x in range(20):
    a,b=b,a+b
    ##print(a)
    if a % 2 == 1:
        jishu.append(a)
    else:
        oushu.append(a)
print(jishu)
print(oushu)
print("奇数有",len(jishu),"个")
print("偶数有",len(oushu),"个")