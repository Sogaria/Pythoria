from turtle import Screen, Turtle
import time
from snake import Snake

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.listen()

gameOn = True

#create snake
snake = Snake()
snake.create_snake()

while gameOn == True:
    window.update()
    time.sleep(0.1)
    #snake movement
    snake.move_snake()
window.mainloop()