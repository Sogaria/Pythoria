from turtle import Turtle
from random import randint
from math import sqrt

class Food:
    def __init__(self):
        self.food_list = []
        self.food_eaten = 0
        self.first_food = (randint(-14, 14) * 20, randint(-14, 14) * 20)


    def create_food(self):
        food = Turtle("circle")
        food.color("green")
        food.teleport(randint(-14, 14) * 20, randint(-14, 14) * 20)
        self.food_list.append(food)

    def food_relocation(self, snake_head_position):
        food_position = self.food_list[0].pos()
        distance = sqrt((food_position[0] - snake_head_position[0]) ** 2 +
                        (food_position[1] - snake_head_position[1]) ** 2)
        
        if distance <= 15:
            self.food_eaten += 1
            self.food_list[0].teleport(randint(-14, 14) * 20, randint(-14, 14) * 20)


#create method to spawn additional snake part in snake.py
#place it behind last element

#in food access this method and call it when food_relocation triggered and score wents up

