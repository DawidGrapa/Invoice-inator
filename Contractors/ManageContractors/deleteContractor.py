import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Database.db import Database

db = Database('Database/Database.db')

class DeleteContractor:
    def __init__(self, window, selected):


