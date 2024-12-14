from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.home()
        self.penup()
        #self.setheading(random.randint(120, 240))
        self.setheading(180)
    
    def move_ball(self, speed):
        self.forward(speed)
    
    def bounce_ball(self, hit_paddle):
        if hit_paddle:
            self.setheading(180 - self.heading())

        if abs(self.pos()[0]) >= 480:
            self.setheading(180 - self.heading())
        
        if abs(self.pos()[1]) >= 315:
            self.setheading(360 - self.heading())