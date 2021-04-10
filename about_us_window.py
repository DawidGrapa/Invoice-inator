from tkinter import *


def open_about_us_window(app):
    # Creating new window
    newWindow = Toplevel(app)
    newWindow.title("About us")
    newWindow.geometry('260x280')
    newWindow.resizable(0, 0)
    newWindow['bg'] = '#f8deb4'

    frame = LabelFrame(newWindow, width=240, height=270, bg='#f8deb4', relief=FLAT)
    frame.pack(padx=10, pady=10)

    x = StringVar()
    x.set("Lolol Manager v0.1 \n\n Authors: \n Dawid Grapa & Julia Szpak \n\n April 2021")

    text = Text(frame, bg="#f8deb4", font="Times 13")
    text.insert(INSERT, x.get())
    text.config(state=DISABLED)
    text.pack()
