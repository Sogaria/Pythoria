from turtle import Turtle

class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def draw_level(self, stage: int):
        self.clear()
        self.teleport(-350, 180)
        self.write(f"Level: {stage}", font=('Arial', 50, 'bold'))

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=('Arial', 50, 'bold'))