# # # # # # # # # # # # # def rect_area(width,height):
# # # # # # # # # # # # #     area = width * height
# # # # # # # # # # # # #     return area
# # # # # # # # # # # #
# # # # # # # # # # # # def print_area(width,height):
# # # # # # # # # # # #     area = width * height
# # # # # # # # # # # #     print("{}*{}长方形的面积：{}".format(width,height,area))
# # # # # # # # # # #
# # # # # # # # # # # # 定义函数-形参
# # # # # # # # # # # def rect_area(width,height):
# # # # # # # # # # #     area = width * height
# # # # # # # # # # #     return area
# # # # # # # # # # #
# # # # # # # # # # # # 函数的调用-实参
# # # # # # # # # # # print("矩形的面积是：",rect_area(100,200))
# # # # # # # # # # def make_coffee(name="卡布奇诺"):
# # # # # # # # # #     return "制作一杯{}咖啡".format(name)
# # # # # # # # # # coffee1 = make_coffee("拿铁")
# # # # # # # # # # coffee2 = make_coffee()
# # # # # # # # # # print(coffee1)
# # # # # # # # # # print(coffee2)
# # # # # # # # #
# # # # # # # # # def sum(*num):
# # # # # # # # #     total = 0
# # # # # # # # #     for i in num:
# # # # # # # # #         total += i
# # # # # # # # #     return total
# # # # # # # # #
# # # # # # # # # print(sum(1,2,3))
# # # # # # # # # print(sum(1,2,3,4,5))
# # # # # # # #
# # # # # # # # def show_info(**info):
# # # # # # # #     for key,value in info.items():
# # # # # # # #         print("{}-{}".format(key,value))
# # # # # # # # show_info(name = "Jack",age = 18,sex = "male")
# # # # # # #
# # # # # # # x = 20 # 在模块中定义的变量，作用域是整个模块
# # # # # # # def print_value():
# # # # # # #     x = 10 # 在函数内部定义的变量，作用域仅仅是此函数，它会屏蔽模块中的变量
# # # # # # #     print("函数中x = {}".format(x))
# # # # # # # print_value()
# # # # # # # print("全局变量x={}".format(x))
# # # # # # x = 20
# # # # # # def print_value():
# # # # # #     global x
# # # # # #     x = 10
# # # # # #     print("函数中x = {}".format(x))
# # # # # # print_value()
# # # # # # print("全局变量x={}".format(x))
# # # # #
# # # # # def calc(opr):
# # # # #     if opr == "+":
# # # # #         return lambda a,b:(a+b)
# # # # #     else:
# # # # #         return lambda a,b:(a-b)
# # # # # f1 = calc("+")
# # # # # f2 = calc("-")
# # # # # print("10+5={}".format(f1(10,5)))
# # # # # print("10-5={}".format(f2(10,5)))
# # # # def square(x):
# # # #     value = x**2
# # # #     return value
# # # #
# # # # print(square(10))
# # #
# # # print("100")
# #
# # a = lambda x:x**2
# # print(a(3))
#
# def myabs(num):
#     if num < 0:
#         num = -num
#     else:
#         num = num
#     return num
#
# num = int(input("请输入一个数字:"))
# print(myabs(num))

# 加法
add = lambda a,b:a+b
# 减法
sub = lambda a,b:a-b
# 乘法
mul = lambda a,b:a*b
# 除法
div = lambda a,b:a/b