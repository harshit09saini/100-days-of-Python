# Pomodoro Timer
import tkinter as tk

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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Pomodoro Timer")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    mins = int(count / 60)
    secs = count % 60

    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
# window.minsize(400, 600)
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = tk.Label(text="Pomodoro Timer", fg=GREEN,
                       bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=350, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 150, image=tomato_image)
timer_text = canvas.create_text(
    100, 300, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(
    text="Start", command=start_timer, font=(FONT_NAME, 10, "bold"))
start_button.config(padx=10, pady=10)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", font=(
    FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.config(padx=10, pady=10)
reset_button.grid(row=2, column=2)

window.mainloop()
