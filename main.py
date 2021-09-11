import tkinter.messagebox
from tkinter import  *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(fg=GREEN, text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    completion.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN)
        title_label.config(fg=GREEN, text='Work')
        window.lift()
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(fg=RED, text='Break')
        print('long break')
    else:
        count_down(SHORT_BREAK_MIN)
        title_label.config(fg=PINK, text='Break')
        print('short break')
        current = completion.cget('text')
        completion.config(text=current + '✓')
        window.lift()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    global timer
    t_minute = math.floor(time/60)
    t_second = time%60

    # REFORMATS time value under 10 seconds to a double digit
    if t_second < 10:
        t_second = '0' + str(t_second)

    canvas.itemconfig(timer_text, text=f"{t_minute}:{t_second}")

    if time > 0:
        timer = window.after(1000, count_down, time-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.attributes('-topmost', True)
window.after_idle(window.attributes, '-topmost', False)
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(bg=YELLOW, fg=GREEN, text='Timer', font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

completion = Label(bg=YELLOW, fg=GREEN, text='', font=(FONT_NAME, 20, 'bold'))
completion.grid(row=3, column=1)

window.mainloop()