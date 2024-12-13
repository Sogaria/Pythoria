from turtle import Screen, Turtle
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.listen()

snake_parts = []
def create_snake():
    for i in range(0, 3):
        snake_parts.append(Turtle("square"))
        snake_parts[i].penup()
        snake_parts[i].setheading(0)
        snake_parts[i].color("white")
        x = -20 + i * 20
        snake_parts[i].goto(x, 0)

def move_snake():
    for i in range(len(snake_parts)-1, 0, -1):    
        pos = snake_parts[i-1].pos()        
        snake_parts[i].teleport(pos[0], pos[1])
    snake_parts[0].forward(20)
    pos = snake_parts[0].pos()
    if abs(pos[0]) >= 300:
        snake_parts[0].teleport(pos[0] * -1, pos[1])
    elif abs(pos[1]) >= 300:
        snake_parts[0].teleport(pos[0], pos[1] * -1)

def turn_left():
    heading = snake_parts[0].heading()
    snake_parts[0].setheading(heading+90)

def turn_right():
    heading = snake_parts[0].heading()
    snake_parts[0].setheading(heading-90)

gameOn = True
create_snake()
while gameOn == True:
    move_snake()
    window.onkeyrelease(lambda: turn_left(), "a")
    window.onkeyrelease(lambda: turn_right(), "d")

window.mainloop()