from datetime import datetime
from tkinter import *

root = Tk()
root.configure(bg='black')
root.title('It is time to make acquaintances')
mylabel1 = Label(root, text="Hello Friend", background='black', fg='green')
mylabel1.pack(fill='both', pady='10', side=TOP, expand='yes')

mylabel2 = Label(root, text="Tell me your Name,friend", background='black', fg='green')
mylabel2.pack(fill='both', pady='10', side=TOP, expand='yes')

e1 = Entry(root, width=50)
e1.pack(side=TOP)


def myclick():
    mylabel3 = Label(root, text="Nice to meet you..." + e1.get(), background='black', fg='green')
    mylabel3.pack(fill='both', pady='10', side=TOP, expand='yes')


mybutton = Button(root, text="Enter", command=myclick)
mybutton.pack(side=TOP)

root.mainloop()