import tkinter as tk

THEME_COLOR = "#375362"

class Ui_Interface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.label = tk.Label(text="Score: 0", background=THEME_COLOR, font=("Arial", 30, "bold"), fg="white")
        self.label.grid(row=0, column=1, pady=30)

        self.canvas = tk.Canvas(background="white", width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.canvas_text = self.canvas.create_text(150, 125, text="Placeholder Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        
        self.photo_true = tk.PhotoImage(file="images/true.png")
        self.button_yes = tk.Button(image=self.photo_true, highlightthickness=0, bd=0)
        self.button_yes.grid(row=2, column=0, pady=20)

        self.photo_false = tk.PhotoImage(file="images/false.png")
        self.button_no = tk.Button(image=self.photo_false, highlightthickness=0, bd=0, anchor="center")
        self.button_no.grid(row=2, column=1, pady=20, padx=(50, 0))

    def update_canvas(self, new_question: str):
        self.canvas.itemconfig(self.canvas_text, text=new_question)
    
    def update_score(self, score: int):
        self.label.config(text=f"Score: {score}")
