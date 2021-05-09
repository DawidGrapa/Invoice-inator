from datetime import date
from tkinter import *


def open_about_us_window(app):
    # Creating new window
    window = Toplevel(app)
    window.title("About us")
    window.geometry('260x150')
    window.resizable(0, 0)
    window['bg'] = '#f8deb4'

    frame = LabelFrame(window, width=240, height=270, bg='#f8deb4', relief=FLAT)
    frame.pack(padx=10, pady=10)

    sv = StringVar()
    sv.set("TBD Manager v0.1 \n\n Authors: \n Dawid Grapa & Julia Szpak \n\n April 2021")

    text = Text(frame, bg="#f8deb4", font="Times 13")
    text.insert(INSERT, sv.get())
    text.config(state=DISABLED)
    text.pack()
