from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import os
import time
import pygame

t = 0
music = False


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
    global music
    music = True
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music
        if music:
            pygame.mixer.music.stop()
            music = False
        label.config(text='set the new remind-time')

pygame.mixer.init()
window = Tk()
window.title('Reminder')
window.config(bg='#D8BFD8')
label = Label(text='Click the button\nbelow to set\nthe reminder time', width=30, height=10, font=('Arial', 14), bg='#ffe3f2')
label.pack(pady=10)
set_button = Button(text='set\nthe reminder', command=set, width=20, height=2, font=('Arial', 12), bg = '#FF69B4', fg='white')
set_button.pack(pady=(5, 55))
stop_button = Button(text='stop the music', command=stop_music)

check()

window.mainloop()

