from turtle import Screen, Turtle

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.listen()

snake_parts = []
def create_snake():
    for i in range(0, 4):
        snake_parts.append(Turtle("square"))
        snake_parts[i].penup()
        snake_parts[i].color("white")
        x = -20 + i * 20
        snake_parts[i].goto(x, 0)

def move_snake():
    for square in snake_parts:
        square.forward(10)
        pos = square.pos()
        #print(f"x: {pos[0]}, y: {pos[1]}")
        if abs(pos[0]) >= 300:
            square.teleport(pos[0] * -1, pos[1])
        elif abs(pos[1]) >= 300:
            square.teleport(pos[0], pos[1] * -1)

def turn_left(snake_parts: list):
    for square in snake_parts:
        heading = square.heading()
        print(heading)

def turn_right(snake_parts: list):
    for square in snake_parts:
        square.right(90)

gameOn = True
create_snake()
while gameOn == True:
    move_snake()
    window.onkeypress(lambda: turn_left(snake_parts), "a")
    window.onkeypress(lambda: turn_right(snake_parts), "d")

window.mainloop()