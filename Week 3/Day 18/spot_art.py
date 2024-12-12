import colorgram
from turtle import Turtle, Screen
import random

screen = Screen()
bob = Turtle()
bob.hideturtle()
screen.colormode(255)
screen.bgcolor(190,190,190)
colors = colorgram.extract("Week 3/Day 18/color_spots.jpg", 12)

def rgb_tuple_list():
    list_colors = []
    colors = colorgram.extract("Week 3/Day 18/color_spots.jpg", 12)
    for item in colors:
        tuple_color = (item.rgb[0], item.rgb[1], item.rgb[2])
        list_colors.append(tuple_color)
    return list_colors

def create_spots():
    bob.penup()
    bob.goto(-350, 350)
    pos = bob.pos()
    bob.penup()
    i = 0
    colors = rgb_tuple_list()
    for row in range(0, 10):
        for dot in range(0, 10):
            print("dot placed")
            bob.dot(50, random.choice(colors))
            i += 1
            bob.forward(77)
        bob.goto(pos[0], pos[1] - 77 - (77*row))

create_spots()
screen.mainloop()

