import tkinter as tk
import string, random, json
from tkinter import messagebox

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
    answer = messagebox.askokcancel(title="Confirmation", message="Confirm saving your data to data.json")
    if answer:
        if input_website.get() == "" or input_email.get() == "" or input_pw == "":
            messagebox.Message(message="Please fill out all inputs.", title="Error").show()
        else:
            messagebox.Message(message="Password successfully stores in data.json!", title="Success!").show()
            
            new_data = {
                input_website.get(): {
                    "Email" : input_email.get(),
                    "Pw" : input_pw.get()
                }
            }
            
            while True:
                try:
                    with open("data.json", mode="r") as file:
                        try:
                            data = json.load(file)
                            data.update(new_data)
                            break
                        except Exception:
                            data = new_data
                            break
                except FileNotFoundError:
                    with open("data.json", "w") as file:
                        pass
                
            
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
                input_email.delete(0, 'end')
                input_pw.delete(0, 'end')
                input_website.delete(0, 'end')
    else: 
        pass
#----------------------Search Website Data--------------------------#
def search_website():
    found = False
    if input_website.get() != "":
        website = input_website.get()
    else:
        messagebox.Message(message="You must enter a website before using search.", title="Error").show()
        return

    try:
        with open("data.json") as file:
            current_data = json.load(file)
        
        for key in current_data:
            if key.lower().find(website.lower()) > -1:
                messagebox.Message(message=f"Website: {website}\nUser: {current_data[key]["Email"]}\nPw: {current_data[key]["Pw"]}", title="Data Information").show()
                found = True
        if not found:
            messagebox.Message(message="Website not found.", title="Error").show()
    except FileNotFoundError:
        messagebox.Message(message="No data found.", title="Error").show()
#----------------------UI Setup--------------------------#
label_website = tk.Label(text="Website:", font=("Arial", 13))
label_website.grid(row=1, column=0)
label_email = tk.Label(text="Email/Username:", font=("Arial", 13))
label_email.grid(row=2, column=0)
label_pw = tk.Label(text="Password:", font=("Arial", 13))
label_pw.grid(row=3, column=0)

input_email = tk.Entry(width=40)
input_email.grid(row=2, column= 1)
input_website = tk.Entry(width=40)
input_website.grid(row=1, column=1)
input_pw = tk.Entry(width=40)
input_pw.grid(row=3, column=1)

button_search = tk.Button(text="Search Data", width=20, command=search_website)
button_search.grid(row=1, column=2)
button_pw = tk.Button(text="Generate Password", command=generate_password, width=20)
button_pw.grid(row=3, column=2)
button_add = tk.Button(text="Add Password to Manager", command=save_data, width=20)
button_add.grid(row=2, column=2)

canvas = tk.Canvas(width=200, height=200)
background = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(row=0, column=1)

window.mainloop()