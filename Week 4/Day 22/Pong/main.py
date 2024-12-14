from turtle import Screen
import time, arena_layout, player_paddle, ball, npc_paddle


window = Screen()
window.bgcolor("black")
window.colormode(255)
window.setup(width=1000, height=650)
window.title("Pong Arcade Game")
window.tracer(0)
window.listen()

gameOn = True
player = player_paddle.Player()
npc = npc_paddle.Npc()
arena = arena_layout.Arena()
arena.draw_arena()
ball = ball.Ball()

window.onkeypress(lambda: player.move_up(), "w")
window.onkeypress(lambda: player.move_down(), "s")

while gameOn:
    window.update()
    time.sleep(0.025)
    ball.move_ball(30)
    npc.follow_ball(ball.pos()[1])

window.mainloop()
#ycor 270 = paddle limitation