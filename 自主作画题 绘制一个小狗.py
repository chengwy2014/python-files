#2
from turtle import *

screensize(600, 600)
# 【头部轮廓】
pensize(5)
home()
seth(0)
pd()
color('black')
circle(20, 80)  # 0
circle(200, 30)  # 1
circle(30, 60)  # 2
circle(200, 29.5)  # 3
color('black')
circle(20, 60)  # 4
circle(-150, 22)  # 5
circle(-50, 10)  # 6
circle(50, 70)  # 7
# 确定鼻头大概位置
x_nose = xcor()
y_nose = ycor()
circle(30, 62)  # 8
circle(200, 15)  # 9
# 【鼻子】
pu()
goto(x_nose, y_nose + 25)
seth(90)
pd()
begin_fill()
circle(8)
end_fill()
# 【眼睛】
pu()
goto(x_nose + 48, y_nose + 55)
seth(90)
pd()
begin_fill()
circle(8)
end_fill()
# 【耳朵】
pu()
color('#444444')
goto(x_nose + 100, y_nose + 110)
seth(182)
pd()
circle(15, 45)  # 1
color('black')
circle(10, 15)  # 2
circle(90, 70)  # 3
circle(25, 110)  # 4
rt(4)
circle(90, 70)  # 5
circle(10, 15)  # 6
color('#444444')
circle(15, 45)  # 7
# 【身体】
pu()
color('black')
goto(x_nose + 90, y_nose - 30)
seth(-130)
pd()
circle(250, 28)  # 1
circle(10, 140)  # 2
circle(-250, 25)  # 3
circle(-200, 25)  # 4
circle(-50, 85)  # 5
circle(8, 145)  # 6
circle(90, 45)  # 7
circle(550, 5)  # 8
# 【尾巴】
seth(0)
circle(60, 85)  # 1
circle(40, 65)  # 2
circle(40, 60)  # 3
lt(150)
circle(-40, 90)  # 4
circle(-25, 100)  # 5
lt(5)
fd(20)
circle(10, 60)  # 6
# 【背部】
rt(80)
circle(200, 35)
# 【项圈】
pensize(20)
color('#D15FEE')
lt(10)
circle(-200, 25)  # 5
# 【爱心铃铛】
pu()
fd(18)
lt(90)
fd(18)
pensize(6)
seth(35)
color('#FFD700')
begin_fill()
lt(135)
fd(6)
right(180)  # 画笔掉头
circle(6, -180)
backward(8)
right(90)
forward(6)
circle(-6, 180)
fd(15)
end_fill()
# 【前小腿】
pensize(5)
pu()
color('black')
goto(x_nose + 100, y_nose - 125)
pd()
seth(-50)
fd(25)
circle(10, 150)
fd(25)
# 【后小腿】
pensize(4)
pu()
goto(x_nose + 314, y_nose - 125)
pd()
seth(-95)
fd(25)
circle(-5, 150)
fd(2)
hideturtle()
done()
