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


def draw(distance, size):
    angle = 360 / size
    for _ in range(size):
        tim.forward(distance)
        tim.right(angle)
    tim.pencolor(color())


shapes = [
    "triangle", "square", "pentagon", "hexagon",
    "heptagon", "octagon", "nonagon", "decagon"
]

for shape in shapes:
    if shape == "triangle":
        draw(100, 3)

    elif shape == "square":
        draw(100, 4)

    elif shape == "pentagon":
        draw(100, 5)

    elif shape == "hexagon":
        draw(100, 6)

    elif shape == "heptagon":
        draw(100, 7)

    elif shape == "octagon":
        draw(100, 8)

    elif shape == "nonagon":
        draw(100, 9)

    elif shape == "decagon":
        draw(100, 10)

screen.exitonclick()