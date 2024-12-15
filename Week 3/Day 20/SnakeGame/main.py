from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

window = Screen()
window.setup(width=680, height=680)
window.bgcolor("black")
window.title("Snake")
window.listen()

gameOn = True

window.tracer(0)
snake = Snake()
snake.create_snake()
snake.draw_border()
food = Food()
food.create_food()
score = Score()
score.write_score(0)

window.onkey(lambda: snake.turn_snake("left"), "a")
window.onkey(lambda: snake.turn_snake("down"), "s")
window.onkey(lambda: snake.turn_snake("right"), "d")
window.onkey(lambda: snake.turn_snake("up"), "w")

while gameOn == True:
    window.update()
    time.sleep(0.1)
    food_eaten = food.food_eaten
    snake.move_snake()
    if snake.check_collissions():
        score.game_over()
        window.update()
        score.score_reset()
        snake.reset_sake()
        food.reset_food_score()
        time.sleep(2)
        score.write_score(food.food_eaten)      
    food.food_relocation(snake.snake_parts[0].pos())
    if food.food_eaten > food_eaten:
        snake.addtional_snake_part()
        score.write_score(food.food_eaten)

window.mainloop()