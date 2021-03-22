from tkinter import *
from Invoice import *

def create():
    label = Label(root, text="CIEKAWE")
    label.pack()

root = Tk()

createInvoice = Button(root, text="Create Invoice",command=create)
createInvoice.pack()
root.mainloop()