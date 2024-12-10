from random_word import RandomWords

def GenerateWord() -> str:
    r = RandomWords()
    return r.get_random_word()

def DisplayWord(liste: list):
    for item in liste:
        print(item, end=" ")

def EmptyWord(word: str) -> list:
    liste = []
    for char in word:
        liste.append("_")
    return liste

def CheckWordChar(word: str, guess: str) -> list:
    index = 0
    list_index = []
    for char in word:
        if char == guess:
            list_index.append(index)
        index += 1
    return list_index

new_Word = GenerateWord()
list_guessing_word = EmptyWord(new_Word)
life = 6
while True:
    for item in list_guessing_word:
        print(item, end=" ")
    guessChar = input("\nWhat letter do you want to guess? ")
    if len(CheckWordChar(new_Word, guessChar)) == 0:
        life -= 1
        print(f"\nWrong guess. You lost a life. {life} remaining.\n")
    else:
        for item in CheckWordChar(new_Word, guessChar):
            list_guessing_word[item] = guessChar
    if list_guessing_word.count("_") == 0:
        for item in list_guessing_word:
            print(item, end=" ")
        print(f"\n\nCongratulations. You won! You had {life} lifes remaining.")
        break
    if life == 0:
        print("\n\nThe hangman got hung.. you suck!!")
        break
#index return working -> to do, handle input and replace _ with correct guess
#implement amount of tries, win or loose
#print out statements until win