from tkinter import *
from time import strftime

root = Tk()
root.title('Clock')
root.configure(background="black")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font= ('calibri', 95, 'bold'),
            background='black',
            foreground='green')
lbl.place(x=0, y=0, relwidth=1, relheight=1)
lbl.pack(anchor='center', expand='YES')


time()
root.mainloop()
