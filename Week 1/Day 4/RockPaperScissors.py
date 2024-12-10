import random
while True:
    playAgain = int(input("Rock 0, Paper 1, Scissors 2. Quit: 3"))
    if playAgain == 3: break
    
    pc = random.randint(0, 2)
    if playAgain == 0:
        if pc == 0:
            print("Pc chose Rock. Draw!")
        elif pc == 1:
            print("Pc chose Paper. Paper beats Rock, you lost!")
        elif pc == 2:
            print("Pc chose Scissors. Rock beats scissors. You won!")
    
    if playAgain == 1:
        if pc == 0:
            print("Pc chose Rock. Rock looses to Paper, you won!")
        elif pc == 1:
            print("Pc chose Paper. Draw!")
        elif pc == 2:
            print("Pc chose Scissors. Scissors beat Paper. You lost!")
    
    if playAgain == 2:
        if pc == 0:
            print("Pc chose Rock. Rock beats Scissors, you lost!")
        elif pc == 1:
            print("Pc chose Paper. Paper looses to Scissors, you won!")
        elif pc == 2:
            print("Pc chose Scissors. Draw!")
    