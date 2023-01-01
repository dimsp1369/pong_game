from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong. Pro")
screen.tracer(0)
screen.listen()

# devider = Turtle("square")
# devider.color("white")
# devider.penup()
# devider.shapesize(1, 0.5, 1)

is_game_on = True

player_1 = Paddle()
player_2 = Paddle(True)

ball = Ball()

score = Score()
screen.onkeypress(player_1.up, "Up")
screen.onkeypress(player_1.down, "Down")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    if ball.out:
        time.sleep(0.5)
        ball.set_out(False)
    else:
        if ball.ycor() >= 280:
            ball.vector("top")
        elif ball.ycor() <= -280:
            ball.vector("bottom")
        if ball.distance(player_2) <= 50 and ball.xcor() > 340:
            ball.hitted_to("right")
        elif ball.distance(player_1) <= 50 and ball.xcor() < -340:
            ball.hitted_to("left")
        ball.move()

        if ball.xcor() >= 390 or ball.xcor() <= -390:
            if ball.paddle == "left":
                score.player_1_ball()
            else:
                score.player_2_ball()
            ball.set_out(True)
            ball.home()
            ball.speed()

        player_2.auto_move()

screen.exitonclick()
