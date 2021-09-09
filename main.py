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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(70)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    t_minute = math.floor(time/60)
    t_second = time%60
    canvas.itemconfig(timer_text, text=f"{t_minute}:{t_second}")
    if time > 0:
        window.after(1000, count_down, time-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
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

reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)

completion = Label(bg=YELLOW, fg=GREEN, text='✓', font=(FONT_NAME, 20, 'bold'))
completion.grid(row=3, column=1)

window.mainloop()