from turtle import Turtle
import random, time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.home()
        self.penup()
        self.ball_speed = 10
        self.setheading(random.randint(120, 240))
        self.lastbounce = 0
        self.currenttime = 0
        self.cooldown = 0.3
    
    def move_ball(self):
        self.forward(self.ball_speed)
    
    def bounce_ball(self, hit_paddle, paddle_distance):
        self.currenttime = time.time()
        if hit_paddle and self.currenttime - self.lastbounce > self.cooldown:
            self.lastbounce = self.currenttime
            self.ball_speed = 5
            self.setheading(180 - self.heading() + paddle_distance)
            self.ball_speed *= (1 + (paddle_distance * 0.05))

        elif hit_paddle == False and abs(self.pos()[1]) >= 315:
            self.setheading(360 - self.heading() + paddle_distance)
    
    def reset_ball(self):
        self.home()
        self.ball_speed = 10
        random_heading = [random.randint(140, 220), random.randint(320, 400)]
        self.setheading(random.choice(random_heading))