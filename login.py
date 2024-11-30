import tkinter as tk

import tkinter.messagebox

username = ["root",]
userpwd = ["123456",]

# 创建一个Tkinter窗口
window = tk.Tk()
window.title("用户登录界面")
window.geometry("300x200+860+408")
window.attributes('-toolwindow', 1)  # 隐藏窗口控制按钮
# window.attributes('-topmost', True)  # 窗口置顶，防止被其他窗口遮挡
window.resizable(False, False)  # 禁止窗口大小调整
# 创建标签
tk.Label(window, text="用户名").grid(row=0, column=0, pady=10)
tk.Label(window, text="密  码").grid(row=1, column=0, pady=10)
# 创建文本框
name_entry = tk.Entry(window)
pwd_entry = tk.Entry(window, show="*")  # 输入的密码会显示为*
# 将文本框放置在窗口上
name_entry.grid(row=0, column=1, padx=10, pady=10)
pwd_entry.grid(row=1, column=1, padx=10, pady=10)


# 创建登录按钮
def login():
    name = name_entry.get()  # 获取用户名
    pwd = pwd_entry.get()  # 获取密码
    # 在此处添加验证用户名和密码的功能
    if name == username[0] and pwd == userpwd[0]:
        login = True
    elif name == username[1] and pwd == userpwd[1]:
        login = True
    elif name == username[2] and pwd == userpwd[2]:
        login = True
    elif name == username[3] and pwd == userpwd[4]:
        login = True
    else:
        login = False
    if login == True:
        # 弹出消息框，提示登录成功
        tk.messagebox.showinfo(title="登录结果", message="登录成功！%s" % name)
    else:
        tk.messagebox.showerror("错误", "用户名或密码错误，请重试！")


# 将按钮的宽度增加3倍
login_button = tk.Button(window, text="登录", command=login, width=9)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=0)

# 将输入框和按钮居中显示
for i in range(2):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(2, weight=1)

# 将窗口的高度减少三分之一，宽度减少四分之一
window.geometry("240x140")
# 开始运行窗口程序
window.mainloop()