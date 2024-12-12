from turtle import Turtle, Screen
import random

bob = Turtle()
screen = Screen()
screen.colormode(255)
bob.speed(10)

def is_close_to (pos1, pos2, tolerance):
    return abs(pos1[0] - pos2[0]) < tolerance and abs(pos1[1] - pos2[1]) < tolerance

def turtle_square():
    bob.forward(100)
    while not is_close_to(bob.pos(), (0, 0), 15):
        bob.right(90)
        bob.forward(100)

def dashed_line(length: int):
    for x in range(0, length):
        if x % 2 == 0:
            bob.pendown()
            bob.forward(5)
        if x % 2 != 0:
            bob.penup()
            bob.forward(5)

def drawing_art():
    for x in range(3, 11):
        angle = 360 / x
        bob.color(random_color())
        for i in range(0, x):
            bob.forward(100)
            bob.right(angle)

def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk():
    list_angles = [0, 90, 180, 270]
    while abs(bob.pos()[0]) < 1920/2 and abs(bob.pos()[1]) < 1080/2:
        bob.pensize(random.randint(1, 10))
        bob.color(random_color())
        bob.right(random.choice(list_angles))
        bob.forward(50)
        print(bob.pos())

def draw_circle(size: int):
    angle = 360 / 50
    for x in range(0, 50):
        bob.forward(size)
        bob.left(angle)

def spirograph():
    print(f"Drawing spirograph with a speed of {bob.speed()}")
    angle = 360 / 50
    for x in range(0, 50):
        bob.color(random_color())
        bob.circle(100)
        bob.left(angle)

spirograph()
screen.mainloop()