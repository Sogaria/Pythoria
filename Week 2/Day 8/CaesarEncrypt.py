import string
def Encryption(userInput : str, text : str, encryptParameter: int):
    all_lowercase = string.ascii_lowercase
    list_lowercase = []
    for char in all_lowercase:
        list_lowercase.append(char)
    all_uppercase = string.ascii_uppercase
    list_uppercase = []
    for char in all_uppercase:
        list_uppercase.append(char)

    encryptText = []
    if userInput == "encrypt":
        for i in range(0, len(text)):
            if text[i] in list_lowercase:
                if list_lowercase.index(text[i]) + encryptParameter >= len(list_lowercase) - 1:
                    index = list_lowercase.index(text[i]) - len(list_lowercase) + encryptParameter
                    encryptText.append(list_lowercase[index])
                else: 
                    encryptText.append(list_lowercase[(list_lowercase.index(text[i]))+encryptParameter])

            elif text[i] in list_uppercase:
                if list_uppercase.index(text[i]) + encryptParameter >= len(list_uppercase) - 1:
                    index = list_uppercase.index(text[i]) - len(list_uppercase) + encryptParameter
                    encryptText.append(list_uppercase[index])
                else: 
                    encryptText.append(list_uppercase[(list_uppercase.index(text[i]))+encryptParameter])
            else:
                encryptText.append(text[i])
    elif userInput == "decrypt":
        for i in range(0, len(text)):
            if text[i] in list_lowercase:
                if list_lowercase.index(text[i]) - encryptParameter < 0:
                    index = len(list_lowercase) - (encryptParameter - list_lowercase.index(text[i]))
                    encryptText.append(list_lowercase[index])
                else:
                    encryptText.append(list_lowercase[list_lowercase.index(text[i])-encryptParameter])

            elif text[i] in list_uppercase:
                if list_uppercase.index(text[i]) - encryptParameter < 0:
                    index = len(list_uppercase) - (encryptParameter - list_uppercase.index(text[i]))
                    encryptText.append(list_uppercase[index])
                else:
                    encryptText.append(list_uppercase[list_uppercase.index(text[i])-encryptParameter])            
            else:
                encryptText.append(text[i])
    
    print("".join(encryptText))

while True:
    userInput = input("encrypt or decrypt? ")
    text = input("Enter the text you want to change: \n")
    encryptParameter = int(input("What parameter is used for the encryption?"))
    print("Here is your result:")
    print()
    Encryption(userInput, text, encryptParameter)
    choice = input("Go again: 1, Quit: -1 ")
    if choice == -1:
        break

