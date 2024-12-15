from turtle import Turtle

class Score():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.score = 0
        self.highscore = 0

    def write_score(self, score):
        self.score = score
        try:
            with open("Week 3/Day 20/SnakeGame/highscore.txt", mode='r') as file:
                highscore = file.read()
                self.highscore = int(highscore)
        except FileNotFoundError:
            pass
        if self.score > self.highscore:
            self.highscore = self.score
        self.turtle.clear()
        self.turtle.teleport(0, 310)
        self.turtle.pencolor("green")
        self.turtle.write(f"Score: {self.score} Highscore: {self.highscore}", False, align= "center", font=("Arial", 20, "bold"))
    
    def game_over(self):
        self.turtle.teleport(0, 0)
        self.turtle.write("GAME OVER", align="center", font=("Arial", 26, "bold"))
        with open("Week 3/Day 20/SnakeGame/highscore.txt", mode='w') as file:
            file.write(str(self.highscore))

    def score_reset(self):
        self.score = 0