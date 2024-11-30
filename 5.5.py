chinese = int(input("请输入语文的成绩："))
math = int(input("请输入数学的成绩："))
if chinese <=100 and chinese >=0:
    if math <=100 and math >=0:
        if chinese == 100 and math == 100:
            print("可以去迪士尼")
        else:
            print("家里蹲，写作业")
