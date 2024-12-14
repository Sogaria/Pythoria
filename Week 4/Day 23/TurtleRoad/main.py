from turtle import Screen
import player

window = Screen()
window.setup(width=800, height=500)
window.title("Turtle Road")
window.listen()
window.tracer(0)

turtle_player = player.Player()
turtle_player.reset_player_pos()

window.onkey(lambda: turtle_player.move_turtle(), "w")

gameOn = True
while gameOn:
    window.update()

window.mainloop()