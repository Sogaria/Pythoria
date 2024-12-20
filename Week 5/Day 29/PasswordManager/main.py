import tkinter as tk
import string, random

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=500, height=350)
window.config(padx=20, pady=20)

#----------------------Constants--------------------------#
LIST_LOWER = list(string.ascii_lowercase)
LIST_UPPER = list(string.ascii_uppercase)
LIST_NUM = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
LIST_SYM = ["@", "#", "$", "%", "#", "&", "*"]
#----------------------Passwort Generation--------------------------#
def generate_password():
    password_list = []
    random.shuffle(LIST_UPPER)
    random.shuffle(LIST_LOWER)
    random.shuffle(LIST_NUM)
    random.shuffle(LIST_SYM)

    for i in range(0, 4):
        password_list.append(LIST_LOWER[i])
        password_list.append(LIST_UPPER[i])
        password_list.append(LIST_NUM[i])
        password_list.append(LIST_SYM[i])

    random.shuffle(password_list)
    password = "".join(password_list)
    
    input_pw.delete(0, 'end')
    input_pw.insert(0, password)
#----------------------SAVE TO TXT--------------------------#
def save_data():
    with open(file="data.txt", mode="a") as file:
        line = f"Website: {input_website.get()} | Email: {input_email.get()} | Password: {input_pw.get()}\n"
        file.write(line)
#----------------------UI Setup--------------------------#
label_website = tk.Label(text="Website:", font=("Arial", 13))
label_website.grid(row=1, column=0)

label_email = tk.Label(text="Email/Username:", font=("Arial", 13))
label_email.grid(row=2, column=0)

label_pw = tk.Label(text="Password:", font=("Arial", 13))
label_pw.grid(row=3, column=0)

input_email = tk.Entry(width=31)
input_email.grid(row=2, column= 1, sticky="w")

input_website = tk.Entry(width=31)
input_website.grid(row=1, column=1, sticky="w")

input_pw = tk.Entry(width=31)
input_pw.grid(row=3, column=1, sticky="w")

button_pw = tk.Button(text="Generate Password", command=generate_password)
button_pw.grid(row=3, column=2, sticky="w")

button_add = tk.Button(text="Add Password to Manager", command=save_data)
button_add.grid(row=4, column=2, sticky="w")

canvas = tk.Canvas(width=200, height=200)
background = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(row=0, column=1)


window.mainloop()
