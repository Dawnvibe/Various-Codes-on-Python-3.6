from tkinter import *
from tkinter import Button

root = Tk()
root.configure(background="black")

Label1 = Label(root, text="I love Python 3.6 Programming Language", bg="black", fg="green")
Label1.configure(font=("Courier", 23))
Label1.pack()
Label2 = Label(root, text="Im writingmy first Py...And I Love it !!!", bg="black", fg="red")
Label2.configure(font=("Courier", 17))
Label2.pack()
Label3 = Label(root, text="This Product is made by Dawnvibe", bg="black", fg="blue")
Label3.configure(font=("Courier", 9))
Label3.pack(side="bottom")

btn = Button(root,
             bg="black",
             fg="red",
             relief="flat",
             text="Exit",
             command=root.destroy,
             width=15)
btn.pack(side="bottom")

root.mainloop()