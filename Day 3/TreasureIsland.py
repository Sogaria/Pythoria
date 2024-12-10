print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("left or right?")

if direction == "right": print("Game Over.")

elif direction == "left":
    lake = input("swim or wait")
    if lake == "swim": print("Game over.")
    elif lake == "wait":
        door = input("red, blue, or yellow?")
        if door == "yellow": print("Congratulations, you found the treasure and won the game!")
        elif door != "yellow": print("Game Over.")