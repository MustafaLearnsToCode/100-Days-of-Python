from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from line import Line

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")
# screen.onkey(fun=l_paddle.paddle_up, key="w")
# screen.onkey(fun=l_paddle.paddle_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    line.dashed()
    screen.update()
    ball.move()

    r_paddle.update_movement()

    l_paddle.follow_ball(ball)

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
        r_paddle.reset_movement()

    #Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
        r_paddle.reset_movement()

    if scoreboard.l_score == 7 and scoreboard.r_score < 7:
        game_on = False
        scoreboard.game_end_l_win()

    if scoreboard.r_score == 7 and scoreboard.l_score < 7:
        game_on = False
        scoreboard.game_end_r_win()



screen.exitonclick()