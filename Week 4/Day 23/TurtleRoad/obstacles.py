from turtle import Turtle
import random, time



class Obstacles():

    def __init__(self):
        super().__init__()
        self.color_list = ["red", "purple", "yellow", "blue", "green", "orange"]
        self.spawn_cords = []
        self.speed = random.randint(5, 10)
        self.cooldown = 1
        self.last_obstactle_created = 0
        self.init_spawn_cords()
        self.visible_obstacles = []

    def init_spawn_cords(self):
        for i in range (200, -250, -50):
            self.spawn_cords.append((-400, i))
        for i in range (225, -225, -50):
            self.spawn_cords.append((400, i))

    def spawn_turtles(self, time, level):
        if time - self.last_obstactle_created > self.cooldown - level * 0.2:
            turtle = Turtle("square")
            turtle.penup()
            turtle.hideturtle()
            turtle.color(random.choice(self.color_list))
            turtle.shapesize(1,2)
            self.last_obstactle_created = time
            spawn = random.choice(self.spawn_cords)
            turtle.teleport(spawn[0], spawn[1])
            if spawn[0] < 0:
                turtle.setheading(0)
            if spawn[0] > 0:
                turtle.setheading(180)
            self.visible_obstacles.append(turtle)
            turtle.showturtle()

    def move_turtles(self, playerx, playery) -> bool:
        temp_remaining = []
        for obstacle in self.visible_obstacles:
            obstacle.forward(5)
            #check collision player
            if abs(playerx - obstacle.pos()[0]) <= 18 and abs(playery - obstacle.pos()[1]) <= 18:
                return True
            if abs(obstacle.pos()[0]) > 500:
                obstacle.reset()
                obstacle.hideturtle()
                del(obstacle)
            else:
                temp_remaining.append(obstacle)
        self.visible_obstacles = temp_remaining
        return False

