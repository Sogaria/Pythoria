import random
streak = 1
previousNum = -1
while streak < 6:
    randomNum = random.randint(0, 1)
    if randomNum == 0 and previousNum == 0:
        streak += 1
        print("Streak of tails: ", streak)
        
    elif randomNum == 1 and previousNum == 1:
        streak += 1
        print("Streak of heads: ", streak)

    elif randomNum != previousNum:
        streak = 1
        
    previousNum = randomNum

