from turtle import Turtle, Screen, listen

screen = Screen()
bob = Turtle()


def turn_right():
    bob.right(10)

def turn_left():
    bob.left(10)

def move_forward():
    bob.forward(10)

def move_backwards():
    bob.backward(10)

def reset_game():
    bob.reset()

screen.listen()
screen.onkeypress(turn_right, "d")
screen.onkeypress(turn_left, "a")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backwards, "s")
screen.onkey(reset_game, "c")


screen.mainloop()
