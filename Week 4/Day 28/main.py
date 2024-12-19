import tkinter as tk
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- TIMER Variables ------------------------------- # 
after_id = None
timer_running = False
minutes = 25
seconds = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer_running, minutes, seconds
    if timer_running:
        window.after_cancel(after_id)
        canvas.itemconfig(canvas_id, text="25:00")
        minutes = 25
        seconds = 0
        timer_running = False
# ---------------------------- TIMER START ------------------------------- # 
def timer_start():
    global timer_running
    if not timer_running:
        timer_running = True
        update_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def update_timer():
    global after_id, minutes, seconds
    if seconds >= 0:
        seconds -= 1
    if seconds == -1:
        seconds = 59
        minutes -= 1
    time_formatted = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(canvas_id, text=time_formatted)
    if minutes == 0 and seconds == 0:
        timer_reset()
    after_id = window.after(1000, update_timer)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=RED)

label_title = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=RED)
label_title.grid(row=0, column=1)

button_start = tk.Button(text="Start", command=lambda: timer_start(), highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text="Reset", command=lambda: timer_reset(), highlightthickness=0)
button_reset.grid(row=2, column=2)

label_checkmarks = tk.Label(text="", highlightthickness=0, bg=RED)
label_checkmarks.grid(row=3, column=1)

canvas = tk.Canvas(width=200, height=224, bg=RED, highlightthickness=0)
background = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
canvas_id = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()