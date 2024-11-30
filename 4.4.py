from tkinter import *
from tkinter.ttk import Separator

root = Tk
root.title("ch2_26")

myTitle = "YIGERENDEQIJINGLVXING"
myContent = """2016NIAN12YUE,WOYIGERENDINGLEJIPIAOHECHUANPIAO,
KAISHIWODENANJILVXING,FEIJINGDIBAIZAIWANGAGENTINGDEWUSIHUAIYA,
ZAICIWODENGSHANGYOULUNKAISHIWODENANJIZHILV"""

lab1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
lab1.pack(fill=X,padx=5)

lab2 = Label(root,text=myContent)
lab2.pack(padx=10,pady=10)

root.mainloop()
