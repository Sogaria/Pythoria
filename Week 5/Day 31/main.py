import tkinter as tk
import pandas, time, random

BACKGROUND_COLOR = "#B1DDC6"
words_csv = pandas.read_csv("data/french_words.csv")
i = 0

window = tk.Tk()
window.title("Study Languages")
window.configure(background=BACKGROUND_COLOR, padx=40, pady=40)
#-------------------------UI-------------------------#
#canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

id_card_front = canvas.create_image(400, 263, image=card_front)
id_card_back = canvas.create_image(400, 263, image=card_back, state='hidden') 
#store obj id to itemconfig canvas obj
id_language_text = canvas.create_text(400, 180, text="English", font=('Comic Sans MS', 30))
id_word_text = canvas.create_text(400, 280, text=words_csv["English"][i], font=('Arial', 30, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

#buttons
yes_image = tk.PhotoImage(file="images/right.png")
yes_button = tk.Button(image=yes_image, bd=0, highlightthickness=0, command=lambda:flip_card(True))
yes_button.grid(row=1, column=1)

no_image = tk.PhotoImage(file="images/wrong.png")
no_button = tk.Button(image=no_image, highlightthickness=0, bd=0, command=lambda:flip_card(False))
no_button.grid(row=1, column=0)
#--------------------Handle Cards--------------------#
def flip_card(know_word: bool):
    global i, words_csv
    #disable buttons until new card
    no_button.config(state='disabled')
    yes_button.config(state='disabled')
    #flip cards
    canvas.itemconfig(id_card_front, state='hidden')
    canvas.itemconfig(id_card_back, state='normal')
    canvas.itemconfig(id_language_text, text="French", fill="white")
    canvas.itemconfig(id_word_text, text=words_csv["French"][i], fill="white")
    if know_word: #yes button
        words_csv = words_csv.drop(index=i)

    #update window manually before after() method timer
    window.update_idletasks()
    
    window.after(5000, new_card)

def new_card():
    global i, words_csv
    #activate buttons again
    no_button.config(state='active')
    yes_button.config(state='active')
    if len(words_csv) > 1 and i < len(words_csv) - 1:
        i += 1
        canvas.itemconfig(id_word_text, text=words_csv["English"][i], fill="black")
        canvas.itemconfig(id_language_text, text="English", fill="black")
        canvas.itemconfig(id_card_front, state='normal')
        canvas.itemconfig(id_card_back, state='hidden')
    elif i == len(words_csv) - 1:
        i = -1
        new_card()

window.mainloop()