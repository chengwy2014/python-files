# # # # from turtle import *
# # # #
# # # # # 定义绘制圆的函数
# # # # def yuan(r):
# # # #     circle(r)
# # # #
# # # # # for i in range(20,50,10):
# # # # #     circle(i)
# # # # # yuan(20)
# # # # for i in range(20,50,10):
# # # #     yuan(i)
# # # #
# # # # hideturtle()
# # # # done()
# # # from turtle import*
# # #
# # # def triangle(sides):
# # #     for i in range(3):
# # #         fd(sides)
# # #         rt(360/3)
# # #
# # # for i in range(20,70,20):
# # #     triangle(i)
# # #     rt(360/3)
# # #
# # # hideturtle()
# # # done()
# # from turtle import *
# # for i in range(5):
# #     fd(50)
# #     lt(72)
# #     fd(50)
# #     rt(144)
# #
# # hideturtle()
# # done()
# from turtle import *
#
# def pentacle(sides):
#     for i in range(5):
#         fd(sides)
#         lt(72)
#         fd(sides)
#         rt(144)
#
# for i in range(20,70,20):
#     pentacle(i)
#     rt(360/3)
def volume(length,width,height):
    return(length*width*height)

length = int(input("请输入长度:"))
width = int(input("亲输入宽度:"))
height = int(input("请输入高度:"))

print("长方形的体积:",volume(length,width,height))