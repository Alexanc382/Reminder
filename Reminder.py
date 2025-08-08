from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import os
import time
from tkinter.simpledialog import askstring
import pygame

t = 0
music = False


def set():
    global t
    rem = sd.askstring('Reminder time', 'Укажите время в 24-часовом формате (чч:мм)')
    if rem:
        try:
            hour_user = int(rem.split(':')[0])
            minute_user = int(rem.split(':')[1])
            if not 0 <= hour_user <= 23 and 0 <= minute_user <= 59:
                mb.showerror('Error', 'Такого времени не существует')
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour_user,minute=minute_user, second=0, microsecond=0)
            print(dt)
            t = dt.timestamp()
            print(t)
            text = askstring('Text', 'Что надо сделать?')
            smile_grinning_face = chr(0x1F600)
            label.config(text=f'Не забудь {smile_grinning_face} :\n{text}\n{hour_user:02}:{minute_user:02}')
        except Exception as e:
            mb.showerror('Error', f'Ошибочка возникла: "{e}"')
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
    pygame.mixer.music.play(-1)



def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    anticlockwise_open_circle_arrow = chr(0x21BA)
    label.config(text=f'Выбери новое напоминание {anticlockwise_open_circle_arrow}')


pygame.mixer.init()
window = Tk()
window.title('Reminder')
window.config(bg='#D8BFD8')
downwards_two_headed_arrow = chr(0x21A1)
label = Label(text=f'Нажми на кнопку\nниже, чтобы выбрать\nвремя напоминания {downwards_two_headed_arrow*3}', width=30, height=10, font=('Arial', 14), bg='#ffe3f2')
label.pack(pady=10)
set_button = Button(text='Тыкни\nсюда', command=set, width=20, height=2, font=('Arial', 12), bg = '#FF69B4', fg='white')
set_button.pack(pady=(5, 55))
stop_button = Button(text='Завершить музыку', command=stop_music, width=20, height=2, font=('Arial', 12), bg = '#FF69B4', fg='white')
stop_button.pack(pady=(5, 45))

check()

window.mainloop()

