from turtle import Turtle

class Npc(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(480, 0)
        self.color("white")
    
    def follow_ball(self, posy):
        self.goto(480, posy)