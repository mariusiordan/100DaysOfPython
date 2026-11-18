import turtle
import math

screen = turtle.Screen()
screen.title("Dot Face")
screen.bgcolor("black")
screen.setup(800, 800)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw dots in a circle
def draw_dot_circle(radius, number_of_dots, color, dot_size):
    for i in range(number_of_dots):
        angle = 2 * math.pi * i / number_of_dots
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        pen.penup()
        pen.goto(x, y)
        pen.dot(dot_size, color)

# Face outline
draw_dot_circle(200, 100, "yellow", 8)

# Eyes
draw_dot_circle(65, 20, "white", 10)

# Left eye
pen.penup()
pen.goto(-65, 60)
pen.dot(25, "white")
pen.goto(-65, 60)
pen.dot(12, "black")

# Right eye
pen.goto(65, 60)
pen.dot(25, "white")
pen.goto(65, 60)
pen.dot(12, "black")

# Nose
pen.goto(0, 10)
pen.dot(15, "orange")

# Smile
for angle in range(210, 331, 10):
    x = 110 * math.cos(math.radians(angle))
    y = 90 * math.sin(math.radians(angle)) - 40

    pen.penup()
    pen.goto(x, y)
    pen.dot(10, "red")

screen.mainloop()




















screen = Screen()
screen.exitonclick()