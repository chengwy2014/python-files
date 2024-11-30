# # # # # # # # 加法定义
# # # # # # # add = lambda a,b:a+b
# # # # # # #
# # # # # # # # 减法定义
# # # # # # # sub = lambda a,b:a-b
# # # # # # #
# # # # # # # # 乘法定义
# # # # # # # mul = lambda a,b:a*b
# # # # # # #
# # # # # # # # 除法定义
# # # # # # # div = lambda a,b:a/b
# # # # # # #
# # # # # # # while True:
# # # # # # #     num_1 = int(input("请输入第1个数字 = "))
# # # # # # #     num_2 = int(input("请输入第2个数字 = "))
# # # # # # #     opr = input("请输入运算符（+，-，*，/）")
# # # # # # #
# # # # # # #     if opr == "+":
# # # # # # #             print("计算结果 = ",add(num_1,num_2))
# # # # # # #
# # # # # # #     elif opr == "-":
# # # # # # #         print("计算结果 = ",sub(num_1,num_2))
# # # # # # #
# # # # # # #     elif opr == "*":
# # # # # # #         print("计算结果 = ",mul(num_1,num_2))
# # # # # # #
# # # # # # #     elif opr == "/":
# # # # # # #         print("计算结果 = ", div(num_1, num_2))
# # # # # # #     else:
# # # # # # #         print("运算公式输入错误")
# # # # # #
# # # # # # # 加法定义
# # # # # # add = lambda a,b:a+b
# # # # # #
# # # # # # # 减法定义
# # # # # # sub = lambda a,b:a-b
# # # # # #
# # # # # # # 乘法定义
# # # # # # mul = lambda a,b:a*b
# # # # # #
# # # # # # # 除法定义
# # # # # # div = lambda a,b:a/b
# # # # # #
# # # # # # Flag = True
# # # # # #
# # # # # # while Flag:
# # # # # #     num_1 = int(input("请输入第1个数字 = "))
# # # # # #     num_2 = int(input("请输入第2个数字 = "))
# # # # # #     opr = input("请输入运算符（+，-，*，/）")
# # # # # #
# # # # # #     if opr == "+":
# # # # # #             print("计算结果 = ",add(num_1,num_2))
# # # # # #             choose = input("是否继续？Y/y继续，其他退出！")
# # # # # #             if choose == "Y" or choose == "y":
# # # # # #                 Flag = True
# # # # # #             else:
# # # # # #                 Flag = False
# # # # # #
# # # # # #     elif opr == "-":
# # # # # #         print("计算结果 = ",sub(num_1,num_2))
# # # # # #         choose = input("是否继续？Y/y继续，其他退出！")
# # # # # #         if choose == "Y" or choose == "y":
# # # # # #             Flag = True
# # # # # #         else:
# # # # # #             Flag = False
# # # # # #
# # # # # #     elif opr == "*":
# # # # # #         print("计算结果 = ",mul(num_1,num_2))
# # # # # #         choose = input("是否继续？Y/y继续，其他退出！")
# # # # # #         if choose == "Y" or choose == "y":
# # # # # #             Flag = True
# # # # # #         else:
# # # # # #             Flag = False
# # # # # #
# # # # # #     elif opr == "/":
# # # # # #         print("计算结果 = ", div(num_1, num_2))
# # # # # #         choose = input("是否继续？Y/y继续，其他退出！")
# # # # # #         if choose == "Y" or choose == "y":
# # # # # #             Flag = True
# # # # # #         else:
# # # # # #             Flag = False
# # # # # #     else:
# # # # # #         print("运算公式输入错误")
# # # # # #         choose = input("是否继续？Y/y继续，其他退出！")
# # # # # #         if choose == "Y" or choose == "y":
# # # # # #             Flag = True
# # # # # #         else:
# # # # # #             Flag = False
# # # # #
# # # # # num_1 = int(input("请输入第一个数="))
# # # # # num_2 = int(input("请输入第二个数="))
# # # # # num_3 = int(input("请输入第三个数="))
# # # # # print(num_1 + num_2 + num_3)
# # # #
# # # # def sum(*num):
# # # #     total = 0
# # # #     for i in num:
# # # #         total += i
# # # #
# # # #     return total
# # # #
# # # # num_1 = int(input("请输入第一个数="))
# # # # num_2 = int(input("请输入第二个数="))
# # # # num_3 = int(input("请输入第三个数="))
# # # #
# # # # print("三个数的和=",sum(num_1,num_2,num_3))
# # #
# # # num_1 = int(input("请输入第一个数="))
# # # num_2 = int(input("请输入第二个数="))
# # # num_3 = int(input("请输入第三个数="))
# # #
# # # 平均值0 = num_1 + num_2 + num_3
# # # 平均值 = 平均值0 / 3
# # # print("三个数的平均值=" + 平均值)
# # #
# # def sum(*num):
# #     total = 0
# #     for i in num:
# #         total += i
# #
# #     avg = total /3
# #     return total,avg
# #
# # num_1 = int(input("请输入第一个数="))
# # num_2 = int(input("请输入第二个数="))
# # num_3 = int(input("请输入第三个数="))
# #
# # print("三个数的和和三个数的平均值分别对应后面的2个数：",sum(num_1,num_2,num_3))
#
# print("hello,world\nhello,china\nhello,shanghai")

def hello(*str):
    for i in str:
        string = "hello" + str
    return string
str_1 = input("请输入第一个字符串：")
str_2 = input("请输入第二个字符串：")
str_3 = input("请输入第三个字符串：")

print(hello(str_1,str_2,str_3))