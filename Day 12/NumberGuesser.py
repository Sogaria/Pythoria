import random
num = random.randint(1, 100)
def GuessNum(num: int,  tries: int):
    while tries > 0:
        print(f"You have {tries} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        if num == guess:
            print(f"You got it! The answer was {num}.")
            return
        elif num < guess:
            tries -= 1
            if tries == 0:
                print(f"Too high. Game over.  The correct number was {num} :P")
                return
            print(f"Too high! \nGuess again.")
        elif num > guess:
            tries -= 1
            if tries == 0:
                print(f"Too low. Game over. The correct number was {num} :P")
                return
            print(f"Too low! \nGuess again.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    GuessNum(num, 10)
elif difficulty == "hard":
    GuessNum(num, 5)
