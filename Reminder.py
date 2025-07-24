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
            dt = now.replace(hour=hour_user,minute=minute_user, second=0, microsecond=0)
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror('Error', f'Error "{e}" occurred' )


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
    window.after(3000, check)


def play_snd():
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()

pygame.mixer.init()
window = Tk()
window.title('Reminder')
label = Label(text='Please set a reminder:', width=50, height=30)
label.pack(pady=10)
set_button = Button(text='set the reminder', command=set)
set_button.pack()

check()

window.mainloop()

