from turtle import Screen
from pong import Label
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

label = Label((350, 0))
label1 = Label((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(label.go_up, "Up")
screen.onkey(label.go_down, "Down")
screen.onkey(label1.go_upper, "a")
screen.onkey(label1.go_downer, "z")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall on above and downward
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Collision with paddle
    if ball.distance(label) < 100 and ball.xcor() > 320 or ball.distance(label1) < 100 and ball.xcor() < -320:
        ball.x_bounce()

    # leaving by right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()

    # leaving by left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()
