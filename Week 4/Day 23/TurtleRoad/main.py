from turtle import Screen
import player, obstacles, time, level

window = Screen()
window.setup(width=800, height=500)
window.title("Turtle Road")
window.listen()
window.tracer(0)

turtle_player = player.Player()
turtle_player.reset_player_pos()
obstacles = obstacles.Obstacles()
level = level.Level()

window.onkey(lambda: turtle_player.move_up(), "w")
window.onkey(lambda: turtle_player.move_down(), "s")
window.onkey(lambda: turtle_player.move_left(), "a")
window.onkey(lambda: turtle_player.move_right(), "d")

gameOn = True
stage = 1

while gameOn:
    current_time = time.time()
    time.sleep(0.1)
    level.draw_level(stage)
    if turtle_player.pos_verify():
        stage += 1
    window.update()
    obstacles.spawn_turtles(current_time, stage)
    if obstacles.move_turtles(turtle_player.pos()[0], turtle_player.pos()[1]):
        level.game_over()
        gameOn = False
        break
window.mainloop()