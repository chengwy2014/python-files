a = input("请输入参与运算的第一个值：")
a = float(a)
opera = input("请选择您要进行的运算符号：+-*/")
b = input("请输入参与运算的第一个值：")
b = float(b)
if opera == "+":
    c = a + b
elif opera == "-":
    c = a - b
elif opera == "*":
    c = a * b
elif opera == "/":
    c = a / b
else:
    c = "ERROR"
print(c)