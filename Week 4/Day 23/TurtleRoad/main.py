from turtle import Screen
import player, obstacles, time

window = Screen()
window.setup(width=800, height=500)
window.title("Turtle Road")
window.listen()
window.tracer(0)

turtle_player = player.Player()
turtle_player.reset_player_pos()
obstacles = obstacles.Obstacles()

window.onkey(lambda: turtle_player.move_turtle(), "w")

gameOn = True
while gameOn:
    current_time = time.time()
    time.sleep(0.1)
    window.update()
    obstacles.spawn_turtles(current_time)
    obstacles.move_turtles()

window.mainloop()