from tkinter import *

window = Tk()
window.title("ch3_1")
lab1 = Label(window,text="明志科技大学",
             bg="lightyellow")
lab2 = Label(window,text="长庚大学",
             bg="lightgreen")
lab3 = Label(window,text="长庚科技大学",
             bg="lightblue")
lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)

window.mainloop()
