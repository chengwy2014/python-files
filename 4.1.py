from  tkinter import *

for i in range(999999999999999999999999999999999999999999999999999999999999999):
    counter = 0
    def run_counter(digit):
        def counting():
             global counter
             counter += 1
             digit.config(text=str(counter))
             digit.after(1000,counting)
        counting()

    root = Tk()
    root.title ("逐渐增加")
    digit=Label(root,bg="yellow",fg="blue",
                height=3,width=10,
                font="Helvetic 20 bold")
    digit.pack()
    run_counter(digit)

    root.mainloop()
