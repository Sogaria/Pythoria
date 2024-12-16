from turtle import Screen, Turtle
import pandas as pd

window = Screen()
window.title("Guess US States")
window.bgpic("Week 4/Day 25/game/blank_states_img.gif")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

#handle csv
state_data = pd.read_csv("Week 4/Day 25/game/50_states.csv")
print(state_data)

#turtle write state on map
def turtle_write(x: int, y: int, state: str):
    turtle.teleport(x, y)
    turtle.write(state, align="center")

#game
correct_guesses = 0
correct_guess_states = []
prompt = window.textinput("Guess the State", "What's another state name?")
prompt = prompt.title()

if state_data.state.to_list().count(prompt) > 0:
    correct_guesses += 1
    correct_guess_states.append(prompt)
    row = state_data[state_data["state"] == prompt]
    state, x, y = row[["state", "x", "y"]].values[0] #because only 1 row in DataFrame -> pull values from index 0
    turtle_write(x, y, state)    
    
while correct_guesses < 50:
    prompt = window.textinput(f"{correct_guesses}/50 States Correct", "What's another state name?")
    prompt = prompt.title()
    
    if state_data.state.to_list().count(prompt) > 0 and correct_guess_states.count(prompt) == 0:
        correct_guesses += 1
        correct_guess_states.append(prompt)
        row = state_data[state_data["state"] == prompt]
        state, x, y = row[["state", "x", "y"]].values[0]
        turtle_write(x, y, state)
window.mainloop()