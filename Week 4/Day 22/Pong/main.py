from turtle import Screen
import time, arena_layout, player_paddle


window = Screen()
window.bgcolor("black")
window.colormode(255)
window.setup(width=1000, height=650)
window.title("Pong Arcade Game")
window.tracer(0)
window.listen()

gameOn = True
player = player_paddle.Player()
arena = arena_layout.Arena()
arena.draw_arena()

window.onkeypress(lambda: player.move_up(), "w")
window.onkeypress(lambda: player.move_down(), "s")

while gameOn:
    window.update()
    time.sleep(0.025)

window.mainloop()
#ycor 270 = paddle limitation