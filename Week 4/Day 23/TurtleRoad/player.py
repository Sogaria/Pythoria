from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()

    def reset_player_pos(self):
        self.teleport(0, -230)

    def move_up(self):
        if self.heading() != 270:
            self.setheading(90)
            self.goto(self.pos()[0], self.pos()[1] + 10)
    
    def move_left(self):
        if self.heading() != 0:
            self.setheading(180)
            self.goto(self.pos()[0] - 10, self.pos()[1])
            
    def move_right(self):
        if self.heading() != 180:
            self.setheading(0)
            self.goto(self.pos()[0] + 10, self.pos()[1])
    
    def move_down(self):
        if self.heading() != 90:
            self.setheading(270)
            self.goto(self.pos()[0], self.pos()[1] - 10)
    

    def pos_verify(self):
        if self.pos()[1] >= 250:
            self.reset_player_pos()
            return True
        return False