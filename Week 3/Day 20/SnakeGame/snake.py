from turtle import Screen, Turtle
from math import sqrt
import time
class Snake:    
    def __init__(self):
        self.snake_parts = []
        self.last_turn_time = 0
        self.turn_cooldown = 0.1
        
    def create_snake(self):
        for i in range(0, 3):
            snake_part = (Turtle("square"))
            snake_part.penup()
            x = 0 - i*20
            snake_part.teleport(x, 0)
            snake_part.color("green")
            self.snake_parts.append(snake_part)

    def addtional_snake_part(self):
        add_snake = Turtle("square")
        add_snake.penup()
        pos_last_part = self.snake_parts[len(self.snake_parts)-1].pos()
        add_snake.teleport(pos_last_part[0], pos_last_part[1])
        add_snake.color("green")
        self.snake_parts.append(add_snake)

    def draw_border(self):
        border_snake = Turtle()
        border_snake.hideturtle()
        border_snake.teleport(310, 310)
        border_snake.pencolor("white")
        for i in range(0, 4):
            border_snake.right(90)
            border_snake.forward(620)
        print(border_snake.pos())

    def check_collissions(self):
        for i in range(len(self.snake_parts)-1, 0, -1):
            distance = sqrt((self.snake_parts[0].pos()[0] - self.snake_parts[i].pos()[0])**2 + 
                            (self.snake_parts[0].pos()[1] - self.snake_parts[i].pos()[1])**2)
            if distance <= 15:
                return True
        if abs(self.snake_parts[0].pos()[0]) >= 310:
            return True
        if abs(self.snake_parts[0].pos()[1]) >= 310:
            return True
        return False

    def move_snake(self):
        for i in range(len(self.snake_parts)-1, 0, -1):    
            pos = self.snake_parts[i-1].pos()        
            self.snake_parts[i].teleport(pos[0], pos[1])
        self.snake_parts[0].forward(20)
        pos = self.snake_parts[0].pos()

    def turn_snake(self, direction: str):
        current_time = time.time()
        if current_time - self.last_turn_time > self.turn_cooldown:
            self.last_turn_time = current_time
            if direction == "left" and self.snake_parts[0].heading() != 0:
                self.snake_parts[0].setheading(180)
            if direction == "right" and self.snake_parts[0].heading() != 180:
                self.snake_parts[0].setheading(0)
            if direction == "up" and self.snake_parts[0].heading() != 270:
                self.snake_parts[0].setheading(90)
            if direction == "down" and self.snake_parts[0].heading() != 90:
                self.snake_parts[0].setheading(270)