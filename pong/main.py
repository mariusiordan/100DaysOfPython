from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

ryan_player = Paddle((350, 0))
silver_player = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(ryan_player.go_up, "Up")
screen.onkey(ryan_player.go_down, "Down")
screen.onkey(silver_player.go_up, "w")
screen.onkey(silver_player.go_down, "s")

game_on = True
while game_on:
    time.sleep(1)
    screen.update()
    ball.move()

    #detect the collision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with the paddle
    if ball.distance(ryan_player) < 50 and ball.xcor() > 340:
        ball.bounce_x()





screen.exitonclick()