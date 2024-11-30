import random
while True:
    a = random.randint(0,1)
    b = input("0/1/exit")
    b = int(b)
    if a = b:
        c = "yes"
    elif a != b:
        c = "no"
    elif b == "exit":
        print("exit")
        break
    else:
        c = "ERROR"
    print(c)