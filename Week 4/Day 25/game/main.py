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
    
def check_missed_states(list_guessed_states):
    list_all_states = state_data.state.to_list()
    missed_states = []
    
    for state in list_all_states:
        if list_guessed_states.count(state) == 0:
            missed_states.append(state)
    new_Frame = pd.DataFrame(missed_states)
    new_Frame.to_csv("Week 4/Day 25/game/missed_states.csv")
#game
correct_guess_states = []
while len(correct_guess_states) < 50:
    prompt = window.textinput(f"{len(correct_guess_states)}/50 States Correct", "What's another state name?")
    prompt = prompt.title()
    
    if prompt == "Exit":
        check_missed_states(correct_guess_states)
        break
    if state_data.state.to_list().count(prompt) > 0 and correct_guess_states.count(prompt) == 0:
        correct_guess_states.append(prompt)
        row = state_data[state_data["state"] == prompt]
        state, x, y = row[["state", "x", "y"]].values[0]
        turtle_write(x, y, state)




window.mainloop()