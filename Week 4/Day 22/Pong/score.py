from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_turtles = []

    def create_turtles(self):
        score_npc = Turtle()
        score_npc.hideturtle()
        score_npc.teleport(200, 225)
        score_npc.penup()
        score_npc.pencolor("white")
        self.score_turtles.append(score_npc)
        self.score_turtles.append(0) #npc score index 1
        
        score_player = Turtle()
        score_player.hideturtle()
        score_player.teleport(-200, 225)
        score_player.penup()
        score_player.pencolor("white")
        self.score_turtles.append(score_player)
        self.score_turtles.append(0) #player score index 3
    
    def print_score(self):
        self.score_turtles[0].clear()
        self.score_turtles[2].clear()
        self.score_turtles[2].write(self.score_turtles[3], font=('Arial', 50, 'bold'))
        self.score_turtles[0].write(self.score_turtles[1], font=('Arial', 50, 'bold'))

            
    def update_score(self, posx_ball):
        if posx_ball > 0: 
            self.score_turtles[3] += 1 #score player
        if posx_ball < 0:
            self.score_turtles[1] += 1 #score npc
