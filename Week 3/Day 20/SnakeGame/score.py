from turtle import Turtle

class Score():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()

    def write_score(self, score):
        self.turtle.clear()
        self.turtle.teleport(0, 290)
        self.turtle.pencolor("green")
        self.turtle.write(f"Score: {score}", False, align= "center", font=("Arial", 20, "bold"))
    
    def game_over(self):
        self.turtle.teleport(0, 0)
        self.turtle.write("GAME OVER", align="center", font=("Arial", 26, "bold"))

