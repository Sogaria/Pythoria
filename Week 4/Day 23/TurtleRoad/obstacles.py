from turtle import Turtle
import random, time



class Obstacles():

    def __init__(self):
        super().__init__()
        self.color_list = ["red", "purple", "yellow", "blue", "green", "orange"]
        self.spawn_cords = []
        self.speed = random.randint(5, 10)
        self.created_obs = []
        self.cooldown = 0.1
        self.last_obstactle_created = 0

    def init_spawn_cords(self):
        for i in range (250, -300, -50):
            self.spawn_cords.append((-400, i))
        for i in range (225, -275, -50):
            self.spawn_cords.append((400, i))

    def spawn_obstacles(self, currentTime):
        if currentTime - self.last_obstactle_created > self.cooldown:
            self.last_obstactle_created = currentTime
            spawn = random.choice(self.spawn_cords)
            turtle = Turtle()
            turtle.shape("square")
            turtle.shapesize(1, 2)
            turtle.color(random.choice(self.color_list))
            turtle.penup()
            turtle.teleport(spawn[0], spawn[1])
            if spawn[0] < 0:
                turtle.setheading(0)
            if spawn[0] > 0:
                turtle.setheading(180)
            self.created_obs.append(turtle)

    def move_turtle(self):
        for turtle in self.created_obs:
            turtle.forward(1)
        

