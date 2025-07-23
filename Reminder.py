from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from datetime import datetime
import os
import time
import pygame

window = Tk()
window.title('Reminder')
label = Label(text='Please set a reminder')
label.pack(pady=10)
set_button = Button('set the reminder', command=set)
set_button.pack()

