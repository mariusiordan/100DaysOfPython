from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)
tim.speed(0)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    tim.color(color())
    tim.circle(150)
    tim.left(3)







screen.exitonclick()