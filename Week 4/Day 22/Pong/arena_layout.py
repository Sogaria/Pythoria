from turtle import Turtle

class Arena:
    
    def __init__(self):
        pass

    def draw_arena(self):
        turtle = Turtle()
        turtle.teleport(-500, 322)
        turtle.hideturtle()
        turtle.pensize(12)
        turtle.pencolor("white")
        turtle.forward(1000)
        turtle.teleport(-500, -315)
        turtle.forward(1000)

        posy = 304
        for i in range(0, 16):
            turtle = Turtle()
            turtle.color("white")
            turtle.shape("square")
            turtle.shapesize(0.3, 0.5)
            turtle.teleport(0, posy)
            posy -= 40
            print(turtle.pos())
