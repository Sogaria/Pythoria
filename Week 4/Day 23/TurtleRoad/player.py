from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)        
        self.penup()

    def reset_player_pos(self):
        self.teleport(0, -230)

    def move_turtle(self):
        self.goto(0, self.pos()[1] + 10)