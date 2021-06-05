from tkinter import *


# Function to create a small window with info about us - creators:)
def open_about_us_window(app):
    window = Toplevel(app)
    window.title("About us")
    window.resizable(0, 0)
    window['bg'] = '#999999'

    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    window.geometry('%dx%d+%d+%d' % (260, 150, width//2 - 130, height//2 - 75))

    frame = LabelFrame(window, width=240, height=270, bg='#999999', relief=FLAT)
    frame.pack(padx=10, pady=10)

    sv = StringVar()
    sv.set("Invoice-inator v1.0 \n\n Authors: \n Dawid Grapa & Julia Szpak \n\n June 2021")

    text = Text(frame, bg="#D2D2D2", font="Helvetica 13")
    text.insert(INSERT, sv.get())
    text.config(state=DISABLED)
    text.pack()
