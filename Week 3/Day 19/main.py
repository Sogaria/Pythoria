from turtle import Turtle, Screen, listen
import random

screen = Screen()

screen.setup(width = 500, height = 400)
user_guess = screen.textinput("Turtle Race", "Which turtle will be the fastest?")
turtles = {}

def turtle_spawn():
    list_colors = ["purple", "orange", "red", "blue", "black", "pink"]
    y = 155
    for color in list_colors:
        turtles[f"{color}"] = Turtle("turtle")
        turtles[f"{color}"].color(color)
        turtles[f"{color}"].penup()
        turtles[f"{color}"].goto(-220, y)
        y -= (360 / len(list_colors))

def turtle_race():
    winner = ""
    while True:
        for item in turtles:
            turtles[item].forward(random.randint(0, 20))
            if turtles[item].pos()[0] >= 250:
                winner = item
                return winner
turtle_spawn()
winner_turtle = turtle_race()
print(f"The {winner_turtle} turtle won the race!")
if user_guess.lower() == winner_turtle.lower():
    print("Your turtle won! :)")
else:
    print("Your turtle did not win! :C")



screen.mainloop()


