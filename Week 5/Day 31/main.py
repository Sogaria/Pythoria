import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Study Languages")
window.configure(background=BACKGROUND_COLOR, padx=40, pady=40)
#-------------------------UI-------------------------#

#canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
#remember to edit state between 'normal' and 'hidden'
id_card_front = canvas.create_image(400, 263, image=card_front)
id_card_back = canvas.create_image(400, 263, image=card_back, state='hidden') 
#store obj id to itemconfig canvas obj
language_text = canvas.create_text(400, 180, text="French", font=('Comic Sans MS', 30))
word_text = canvas.create_text(400, 280, text="TestWord", font=('Arial', 30, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

#buttons
yes_image = tk.PhotoImage(file="images/right.png")
yes_button = tk.Button(image=yes_image, bd=0, highlightthickness=0)
yes_button.grid(row=1, column=1)

no_image = tk.PhotoImage(file="images/wrong.png")
no_button = tk.Button(image=no_image, highlightthickness=0, bd=0)
no_button.grid(row=1, column=0)
#--------------------Handle Cards--------------------#
words_csv = pandas.read_csv("data/french_words.csv")
#use button yes and no to trigger flip to french word, pass bool to either remove or keep the word in dataframe
        

window.mainloop()
