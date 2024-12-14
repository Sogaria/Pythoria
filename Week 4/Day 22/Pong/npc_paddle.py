from turtle import Turtle

class Npc(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(480, 0)
        self.color("white")
    
    def follow_ball(self, posy, posx):
        if posy > self.pos()[1] and abs(posx - self.pos()[0]) <= 500 and abs(self.pos()[1]) <= 275:
            self.goto(480, self.pos()[1]+10)
        if posy < self.pos()[1] and abs(posx - self.pos()[0]) <= 500 and abs(self.pos()[1]) <= 275:
            self.goto(480, self.pos()[1]-10)