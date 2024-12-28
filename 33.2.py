m = int(input("请输入第一个数"))
n = int(input("请输入第二个数"))
list1 = []
if m > n:
    a = n
else:
    a = m
for i in range(1,19):
    if a % i == 0:
        list1.append(i)
print(list1)