#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
with open("Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
    for line in invited_names:
        names.append(line.strip('\n'))

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.readlines()
    
for str in names:
    with open(f"Mail Merge Project Start/Output/ReadyToSend/{str}.txt", "w") as letters:
        first_line = letter[0]
        first_line = first_line.replace("[name]", str)
        letters.write(first_line)
        for i in range(1, len(letter)):
            letters.write(letter[i])