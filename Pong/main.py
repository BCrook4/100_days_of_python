from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_COORD = (-350, 0)
RIGHT_COORD = (350, 0)
R_GOAL = 400
L_GOAL = -400
WIN_SCORE = 5

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(RIGHT_COORD)
l_paddle = Paddle(LEFT_COORD)
ball = Ball()
scoreboard = Scoreboard()
ball.serve()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.speed_up()


    # detect score scenario (missed hit)
    if ball.xcor() > R_GOAL:
        scoreboard.l_scored()
        ball.serve()

    elif ball.xcor() < L_GOAL:
        scoreboard.r_scored()
        ball.serve()


    if scoreboard.l_score == WIN_SCORE or scoreboard.r_score == WIN_SCORE:
        scoreboard.game_won()
        game_is_on = False



    screen.listen()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")















screen.exitonclick()