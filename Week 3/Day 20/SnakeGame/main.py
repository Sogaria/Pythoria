from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.listen()

gameOn = True

#create snake
snake = Snake()
snake.create_snake()
food = Food()
food.create_food()

window.onkey(lambda: snake.head_up(), "w")
window.onkey(lambda: snake.head_left(), "a")
window.onkey(lambda: snake.head_down(), "s")
window.onkey(lambda: snake.head_right(), "d")

while gameOn == True:
    window.update()
    time.sleep(0.1)
    #snake movement
    food_eaten = food.food_eaten
    snake.move_snake()
    food.food_relocation(snake.snake_parts[0].pos())
    print(food.food_eaten)
    if food.food_eaten > food_eaten:
        snake.addtional_snake_part()

window.mainloop()