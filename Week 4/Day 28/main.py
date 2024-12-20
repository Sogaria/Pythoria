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
CHECKMARK = "✔"
# ---------------------------- TIMER Variables ------------------------------- # 
after_id = None
timer_running = False
minutes = WORK_MIN
seconds = 0
onbreak = False
sets = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset(minutes_reset, second_reset, button_press: bool):
    global timer_running, minutes, seconds
    
    if timer_running and not button_press:
        minutes = minutes_reset
        seconds = second_reset
    if button_press and after_id != None:
        canvas.itemconfig(canvas_id, text="25:00")
        minutes = WORK_MIN
        seconds = 0
        timer_running = False
        window.after_cancel(after_id)
# ---------------------------- TIMER START ------------------------------- # 
def timer_start():
    global timer_running, sets
    
    if not timer_running:
        timer_running = True
        label_title.config(text="Study now c:")
        update_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def update_timer():
    global after_id, minutes, seconds, onbreak, sets

    if seconds >= 0:
        seconds -= 1
    if seconds == -1:
        seconds = 59
        minutes -= 1

    time_formatted = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(canvas_id, text=time_formatted)
    
    if minutes == 0 and seconds == 0:
        if onbreak:
            timer_reset(WORK_MIN, 0, False)
            label_title.config(text="Study now c:")
            onbreak = False
            
        elif not onbreak:
            sets += 1
            if sets % 4 == 0:
                label_title.config(text="Long Break c:")
                timer_reset(LONG_BREAK_MIN, 0, False)
            else:
                label_title.config(text="Short Break c:")
                timer_reset(SHORT_BREAK_MIN, 0, False)
            onbreak = True
            
    label_checkmarks.config(text=(sets * CHECKMARK))
    after_id = window.after(1000, update_timer)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=RED)

label_title = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=RED)
label_title.grid(row=0, column=1)

button_start = tk.Button(text="Start", command=lambda: timer_start(), highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text="Reset", command=lambda: timer_reset(25, 0, True), highlightthickness=0)
button_reset.grid(row=2, column=2)

label_checkmarks = tk.Label(text="", highlightthickness=0, bg=RED, fg=GREEN, font=(30))
label_checkmarks.grid(row=3, column=1)

canvas = tk.Canvas(width=200, height=224, bg=RED, highlightthickness=0)
background = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
canvas_id = canvas.create_text(100, 130, text="25:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()