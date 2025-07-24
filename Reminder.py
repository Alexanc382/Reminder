from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import os
import time
import pygame

t = 0


def set():
    global t
    rem = sd.askstring('Reminder time', 'Enter the reminder-time in 24-hour format(hh:mm)')
    if rem:
        try:
            hour_user = int(rem.split(':')[0])
            minute_user = int(rem.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour_user,minute=minute_user)
            print(dt)
            t = dt.fromtimestamp()
            print(t)
        except Exception as e:
            mb.showerror('Error', f'Error "{e}" occurred' )


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play.snd()
            t = 0
    window.after(10000, check)


window = Tk()
window.title('Reminder')
label = Label(text='Please set a reminder:', width=50, height=30)
label.pack(pady=10)
set_button = Button(text='set the reminder', command=set)
set_button.pack()

window.mainloop()

