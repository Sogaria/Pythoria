from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.teleport(-480, 0)
        self.color("white")
    
    def move_up(self):
        ycor = self.ycor() + 15
        if abs(ycor) <= 270:
            self.goto(self.xcor(), ycor)
        
    def move_down(self):
        ycor = self.ycor() - 15
        if abs(ycor) <= 270:
            self.goto(self.xcor(), ycor)

    def reset_player(self):
        self.teleport(-480, 0)


