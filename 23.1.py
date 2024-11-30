# money = input("money = ")
# money = float(money)
# print("100Yuan = " + str(money // 100))
# money = money % 100
# print("50Yuan = " + str(money // 50))
# money = money % 50
# print("20Yuan = " + str(money // 20))
# money = money % 20
# print("10Yuan = " + str(money // 20))
# money = money % 10
# print("5Yuan = " + str(money // 10))
# money = money % 5
# print("1Yuan = " + str(money // 1))
# money = money % 1
# print("0.5 = " + str(money // 0.5))
# money = money % 0.5
# print("0.1 = " + str(money // 0.1))
money = float(input("money = "))
RMB = [100,50,20,10,5,1,0.5,0.1,0.01]
if money <= 0:
    print("money <= 0")
    exit(0)
for i in range(9):
    a = str(RMB[i]) + "Yuan = "
    b = money // RMB[i]
    if b == 0:
        continue
    print(a + str(b))
    money = money % RMB[i]