from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.home()
        self.penup()
        self.ball_speed = 10
        self.setheading(random.randint(120, 240))
    
    def move_ball(self):
        self.forward(self.ball_speed)
    
    def bounce_ball(self, hit_paddle, paddle_distance):
        if hit_paddle:
            self.ball_speed = 10
            self.setheading(180 - self.heading() + paddle_distance)
            self.ball_speed *= (1 + (paddle_distance * 0.05))

        if abs(self.pos()[0]) >= 480:
            self.setheading(180 - self.heading())
        
        if abs(self.pos()[1]) >= 315:
            self.setheading(360 - self.heading())