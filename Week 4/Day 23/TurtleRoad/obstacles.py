from turtle import Turtle
import random, time



class Obstacles():

    def __init__(self):
        super().__init__()
        self.color_list = ["red", "purple", "yellow", "blue", "green", "orange"]
        self.spawn_cords = []
        self.speed = random.randint(5, 10)
        self.list_of_obstacles = []
        self.cooldown = 1
        self.last_obstactle_created = 0
        self.init_spawn_cords()
        self.create_turtles()
        self.visible_obstacles = []

    def init_spawn_cords(self):
        for i in range (250, -250, -50):
            self.spawn_cords.append((-400, i))
        for i in range (225, -225, -50):
            self.spawn_cords.append((400, i))

    def create_turtles(self):
        for color in self.color_list:
            turtle = Turtle("square")
            turtle.penup()
            turtle.hideturtle()
            turtle.shapesize(1, 2)
            turtle.color(color)
            self.list_of_obstacles.append(turtle)

    def spawn_turtles(self, time):
        if time - self.last_obstactle_created > self.cooldown:
            self.last_obstactle_created = time
            turtle = random.choice(self.list_of_obstacles)
            spawn = random.choice(self.spawn_cords)
            turtle.teleport(spawn[0], spawn[1])
            if spawn[0] < 0:
                turtle.setheading(0)
            if spawn[0] > 0:
                turtle.setheading(180)
            self.visible_obstacles.append(turtle)
            turtle.showturtle()

    def move_turtles(self):
        index = 0
        for obstacle in self.visible_obstacles:
            obstacle.forward(5)
            if abs(obstacle.pos()[0]) > 420:
                self.visible_obstacles.pop(index)
            index += 1
        
            
        

