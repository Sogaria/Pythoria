from turtle import Screen, Turtle

#FIRST_THREE_BODIES = [(20, 0)]
class Snake:
    
    def __init__(self):
        self.snake_parts = []
        
    def create_snake(self):
        for i in range(0, 3):
            snake_part = (Turtle("square"))
            snake_part.penup()
            x = 0 - i*20
            snake_part.teleport(x, 0)
            snake_part.color("white")
            self.snake_parts.append(snake_part)

    def addtional_snake_part(self):
        add_snake = Turtle("square")
        add_snake.penup()
        pos_last_part = self.snake_parts[len(self.snake_parts)-1].pos()
        add_snake.teleport(pos_last_part[0], pos_last_part[1])
        add_snake.color("white")
        self.snake_parts.append(add_snake)

    def check_collissions(self):
        for i in range(len(self.snake_parts)-1, 0, -1):
            if self.snake_parts[i].pos() == self.snake_parts[0].pos():
                return True
        else: 
            return False

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

    def head_up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)
    def head_left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)
    def head_down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)
    def head_right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)