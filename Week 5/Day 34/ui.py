import tkinter as tk

THEME_COLOR = "#375362"

class Ui_Interface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.label = tk.Label(text="Score: 0", background=THEME_COLOR, font=("Arial", 30, "bold"), fg="white")
        self.label.grid(row=0, column=1, pady=30)

        self.canvas = tk.Canvas(background="white", width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.canvas_text = self.canvas.create_text(150, 125, text="Test", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=250, state="normal")
        self.canvas_feedback_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=250, state="hidden")
        
        self.photo_true = tk.PhotoImage(file="images/true.png")
        self.button_yes = tk.Button(image=self.photo_true, highlightthickness=0, bd=0, command=lambda:self.button_press(True))
        self.button_yes.grid(row=2, column=0, pady=20)

        self.photo_false = tk.PhotoImage(file="images/false.png")
        self.button_no = tk.Button(image=self.photo_false, highlightthickness=0, bd=0, command=lambda:self.button_press(False))
        self.button_no.grid(row=2, column=1, pady=20, padx=(50, 0))

        self.update_canvas()
        self.window.mainloop()

    def update_canvas(self):
        if self.quiz.still_has_questions():
            self.update_score()
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=f"Q.{self.quiz.question_number}: " + next_question, state="normal")
            self.canvas.itemconfig(self.canvas_feedback_text, state="hidden")
        else:
            self.ending_screen()
    
    def button_press(self, decision: bool):
        if decision:
            if self.quiz.evaluate_answer(True):
                self.canvas.itemconfig(self.canvas_text, state="hidden")
                self.canvas.itemconfig(self.canvas_feedback_text, state="normal", text="Correct!")
            else:
                self.canvas.itemconfig(self.canvas_text, state="hidden")
                self.canvas.itemconfig(self.canvas_feedback_text, state="normal", text="Incorrect!")

        elif not decision:
            if self.quiz.evaluate_answer(False):
                self.canvas.itemconfig(self.canvas_text, state="hidden")
                self.canvas.itemconfig(self.canvas_feedback_text, state="normal", text="Correct!")
            else:
                self.canvas.itemconfig(self.canvas_text, state="hidden")
                self.canvas.itemconfig(self.canvas_feedback_text, state="normal", text="Incorrect!")
        self.window.after(1000, self.update_canvas)

    
    def update_score(self):
        self.label.config(text=f"Score: {self.quiz.score}")
    
    def ending_screen(self):
        self.button_no.config(state="disabled")
        self.button_yes.config(state="disabled")
        self.canvas.itemconfig(self.canvas_feedback_text, state="hidden")
        self.canvas.itemconfig(self.canvas_text, text=f"Quiz completed. Your score is {self.quiz.score}/10!", state="normal")
