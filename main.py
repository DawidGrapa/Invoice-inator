from tkinter import *
from tkinter.ttk import *
from Contrahents import *

#Create window object
app = Tk()
app['bg']='#f8deb4'
app.title("Apka")

app.state("zoomed")

#Change app icon
photo = PhotoImage(file = 'flow.png')
app.iconphoto(False, photo)

#Create Menu
my_menu = Menu(app)
app.config(menu = my_menu)

file_menu= Menu(my_menu,tearoff = False)
file_menu.add_command(label="Create invoice",font= 'Helvetica 10 bold')
file_menu.add_separator()
file_menu.add_command(label="List of contractors",command = lambda: open_contractors_window(app))
settings_menu = Menu(my_menu,tearoff= False)

my_menu.add_cascade(label="MENU", menu=file_menu)
my_menu.add_separator()
my_menu.add_cascade(label="Settings",menu=settings_menu)



#Start of the program
app.mainloop()