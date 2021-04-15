from Contractors.contractors import *
from PopUpWindows.about_us_window import *
from Products.products import *

# Creating window app
app = Tk()
app.title("TBD Manager")
app.state("zoomed")
app['bg'] = '#f8deb4'
# Change app icon
photo = PhotoImage(file='Media/soy.png')
app.iconphoto(True, photo)

# Creating menu
my_menu = Menu(app)
app.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
file_menu.add_command(label="Create invoice", font='Helvetica 10 bold')
file_menu.add_separator()
file_menu.add_command(label="List of contractors", command=lambda: open_contractors_window(app))
file_menu.add_separator()
file_menu.add_command(label = "List of products", command = lambda: open_products_window(app))

settings_menu = Menu(my_menu, tearoff=False)

help_menu = Menu(my_menu, tearoff=False)
help_menu.add_command(label="Getting started")
help_menu.add_separator()
help_menu.add_command(label="About us", command=lambda: open_about_us_window(app))

my_menu.add_cascade(label="MENU", menu=file_menu)
my_menu.add_cascade(label="Settings", menu=settings_menu)
my_menu.add_cascade(label="Help", menu=help_menu)

# Start of the program
app.mainloop()
