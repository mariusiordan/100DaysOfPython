from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)
tim.speed("fastest")


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#colors = ["red", "orange", "gold", "green", "cyan", "blue", "purple", "magenta"]
directions = [0, 90, 180, 270]
sizes = [10, 15, 20, 25]

for _ in range(1000):
    tim.pencolor(color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pensize(random.choice(sizes))









screen.exitonclick()