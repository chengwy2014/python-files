print("AI石头剪刀布 V2.0")
lever = int(input("选择难度\n1 简单\n2 普通\n3 特难\n"))
a = int(input("1 石头\n2 剪刀\n3 布\n"))
if lever == 1:
    if a == 1:
        print("电脑：剪刀\n你赢了")
    elif a == 2:
        print("电脑：布\n你赢了")
    else:
        print("电脑：石头\n你赢了")
elif lever == 2:
    if a == 1:
        print("电脑：石头\n平局")
    elif a == 2:
        print("电脑：剪刀\n平局")
    else:
        print("电脑：布\n平局")
else:
    if a == 1:
        print("电脑：布\n你输了")
    elif a == 2:
        print("电脑：石头\n你输了")
    else:
        print("电脑：剪刀\n你输了")