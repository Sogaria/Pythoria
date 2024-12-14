from turtle import Screen
import time, arena_layout, player_paddle, ball, npc_paddle, score


window = Screen()
window.bgcolor("black")
window.colormode(255)
window.setup(width=1000, height=650)
window.title("Pong Arcade Game")
window.tracer(0)
window.listen()

player = player_paddle.Player()
npc = npc_paddle.Npc()
arena = arena_layout.Arena()
arena.draw_arena()
score = score.Score()
score.create_turtles()
score.print_score()
ball = ball.Ball()

window.onkeypress(lambda: player.move_up(), "w")
window.onkeypress(lambda: player.move_down(), "s")
gameOn = True

while gameOn == True:
    window.update()
    ball.move_ball()
    time.sleep(0.016)
    ball.bounce_ball(False, 0)
    npc.follow_ball(ball.pos()[1], ball.pos()[0])
    
    if abs(ball.pos()[0]) > 490:
        score.update_score(ball.pos()[0])
        score.print_score()
        ball.reset_ball()
        player.reset_player()
        npc.reset_npc()
        time.sleep(1)
        
    if abs(ball.pos()[0] - player.pos()[0]) <= 35 and abs(ball.pos()[1] - player.pos()[1]) <= 50:
        ball.bounce_ball(True, abs(ball.pos()[1] - player.pos()[1]))
        
    if abs(ball.pos()[0] - npc.pos()[0]) <= 35 and abs(ball.pos()[1] - npc.pos()[1]) <= 50:
        ball.bounce_ball(True, abs(ball.pos()[1] - npc.pos()[1]))


window.mainloop()
