from turtle import Screen, Turtle
class Snake:
    
    def __init__(self):
        self.snake_parts = []
        
    def create_snake(self):
        for i in range(0, 3):
            snake_part = (Turtle("square"))
            snake_part.penup()
            snake_part.color("white")
            x = -20 + i * 20
            snake_part.goto(x, 0)
            self.snake_parts.append(snake_part)

    def move_snake(self):
        for i in range(len(self.snake_parts)-1, 0, -1):    
            pos = self.snake_parts[i-1].pos()        
            self.snake_parts[i].teleport(pos[0], pos[1])
        self.snake_parts[0].forward(20)
        pos = self.snake_parts[0].pos()
        if abs(pos[0]) >= 300:
            self.snake_parts[0].teleport(pos[0] * -1, pos[1])
        elif abs(pos[1]) >= 300:
            self.snake_parts[0].teleport(pos[0], pos[1] * -1)

    def turn_left(self):
        heading = self.snake_parts[0].heading()
        self.snake_parts[0].setheading(heading+90)

    def turn_right(self):
        heading = self.snake_parts[0].heading()
        self.snake_parts[0].setheading(heading-90)
