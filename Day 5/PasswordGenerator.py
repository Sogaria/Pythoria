import string
import random

list_letter = []
for char in string.ascii_lowercase:
    list_letter.append(char)
for char in string.ascii_uppercase:
    list_letter.append(char)

list_numbers = []
for i in range(0, 10):
    list_numbers.append(f"{i}")
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

list_Password = []

for i in range(0, nr_letters):
    random.shuffle(list_letter)
    list_Password.append(list_letter[0])

for j in range(0, nr_symbols):
    random.shuffle(list_symbols)
    list_Password.append(list_symbols[0])
        
for g in range(0, nr_numbers):
    random.shuffle(list_numbers)
    list_Password.append(list_numbers[0])

random.shuffle(list_Password) 
password = "".join(list_Password)

print("Password successfully created: ", password)