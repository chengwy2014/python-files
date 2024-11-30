from turtle import *
from time import *
# speed(1)
# # screensize(600,500,"green")
# setup(0.2,0.3,300,500)
# pensize(5)
# # pencolor("green")
# colormode(1)
# pencolor(0.2,0.5,0.9)
# fd(100)
#
# color(pencolor,fillcolor)
#
#
# color("red","yellow")
#
#
#
#
# done()
# 绘制一个八边形，画笔的粗细为5像素，填充色为黄色，画笔的颜色绿色

# pensize(5)
# pencolor("green")
# fillcolor("yellow")
# for i in range(8):
#     fd(100)
#     rt(360/8)
# endfill()
# for i in range(4):
#     fd(100)
#     rt(360/4)
#
# penup()
# goto(25,-25)
# pendown()
# for i in range(4):
#     fd(50)
#     rt(360/4)
# circle(-100)
# setx(100)
# sety(100)
# setx(0)
# sety(0)
# seth(45)
# fd(100)
seth(90)
for i in range(10,60,10):
    fd(50)
    dot(i,"red")
sleep(2)
clear()


hideturtle()
done()