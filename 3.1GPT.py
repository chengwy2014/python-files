from tkinter import *


# 定义常用的函数
def add_number(number):
    current_number = calc_input.get()
    calc_input.delete(0, END)
    calc_input.insert(0, str(current_number) + str(number))


def add_operator(operator):
    first_number = calc_input.get()
    global f_num
    f_num = int(first_number)
    global math_op
    math_op = operator
    calc_input.delete(0, END)


def calculate():
    second_number = calc_input.get()
    calc_input.delete(0, END)
    if math_op == "+":
        calc_input.insert(0, f_num + int(second_number))
    elif math_op == "-":
        calc_input.insert(0, f_num - int(second_number))
    elif math_op == "*":
        calc_input.insert(0, f_num * int(second_number))
    elif math_op == "/":
        calc_input.insert(0, f_num / int(second_number))


def clear_display():
    calc_input.delete(0, END)
    calc_input.insert(0, 0)


# 创建主窗口
root = Tk()
root.title("简易计算器")

# 创建计算器输入框
calc_input = Entry(root, width=35, borderwidth=5)
calc_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 创建计算器按钮
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_number(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_number(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_number(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_number(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_number(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_number(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_number(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_number(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_number(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_number(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: add_operator("+"))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: add_operator("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: add_operator("*"))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: add_operator("/"))
button_equal = Button(root, text="=", padx=91, pady=20, command=calculate)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear_display)

# 按钮的位置
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

# 运行主循环
root.mainloop()
