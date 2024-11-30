from turtle import *
# 安全
truepassword = ""
input_password = float(input("请输入密码才能运行此程序："))
if input_password == truepassword:
    hideturtle()
    speed(10)
    # 绘制矩形
    penup()
    goto(-200, 200)
    pendown()
    color("red", "red")
    begin_fill()
    for i in range(2):
        # fd(600)
        fd(500)
        rt(90)
        fd(300)
        rt(90)
    end_fill()

    # 绘制大的五级角星

    penup()
    goto(-160, 120)
    pendown()
    color("yellow", "yellow")
    begin_fill()
    for i in range(5):
        fd(40)
        lt(72)
        fd(40)
        rt(144)
    end_fill()

    # 绘制第一个小的五角星
    penup()
    goto(-40, 160)
    pendown()
    color("yellow", "yellow")
    seth(40)
    begin_fill()
    for i in range(5):
        fd(10)
        lt(72)
        fd(10)
        rt(144)
    end_fill()

    # 绘制第二个小的五角星
    penup()
    goto(-10, 130)
    pendown()
    color("yellow", "yellow")
    seth(10)
    begin_fill()
    for i in range(5):
        fd(10)
        lt(72)
        fd(10)
        rt(144)
    end_fill()

    # 绘制第三个小的五角星

    penup()
    goto(-10, 80)
    pendown()
    color("yellow", "yellow")
    seth(0)
    begin_fill()
    for i in range(5):
        fd(10)
        lt(72)
        fd(10)
        rt(144)
    end_fill()

    # 绘制第四个小的五角星

    penup()
    goto(-40, 50)
    pendown()
    color("yellow", "yellow")
    seth(-40)
    begin_fill()
    for i in range(5):
        fd(10)
        lt(72)
        fd(10)
        rt(144)
    end_fill()

    # 写字
    penup()
    # goto(80,-50)
    goto(40, -50)
    pendown()
    write("我爱中国！", font=("楷体", 40,"normal"))
    # hideturtle()
    done()
else:
    print('Your password is not true!Please try it again!')