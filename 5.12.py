import random
player = int(input("请输入你的猜拳数字\n石头=1\n剪刀=2\n布=3\n"))
computer = random.randint(1,3)
print(computer)
if(player == 1 and computer == 2)or(player == 2 and computer == 3)or(player == 3 and computer == 1):
    print("你赢了")
elif player == computer:
    print("平局")
else:
    print("你输了")
