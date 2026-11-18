import turtle
import random

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#101820")
screen.title("Messi - Dot Art")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

random.seed(10)


# Draw dots inside an oval
def dot_oval(cx, cy, rx, ry, color, count, size_min, size_max):
    for _ in range(count):
        x = random.uniform(-rx, rx)
        y = random.uniform(-ry, ry)

        if (x / rx) ** 2 + (y / ry) ** 2 <= 1:
            pen.goto(cx + x, cy + y)
            pen.dot(random.randint(size_min, size_max), color)


# Argentina shirt
dot_oval(0, -270, 175, 120, "#75C9F1", 500, 3, 8)
dot_oval(0, -260, 115, 120, "#FFFFFF", 250, 3, 8)

# Neck
dot_oval(0, -135, 48, 65, "#D69B72", 150, 4, 8)

# Ears
dot_oval(-105, 20, 32, 42, "#D99D79", 120, 4, 8)
dot_oval(105, 20, 32, 42, "#D99D79", 120, 4, 8)

# Face
dot_oval(0, 20, 110, 145, "#E7B28C", 850, 3, 8)

# Hair
dot_oval(0, 145, 112, 48, "#30251F", 350, 3, 9)
dot_oval(-75, 115, 38, 40, "#30251F", 180, 3, 8)
dot_oval(75, 115, 38, 40, "#30251F", 180, 3, 8)

# Beard
dot_oval(0, -65, 105, 75, "#49362C", 500, 3, 8)
dot_oval(0, -95, 80, 40, "#49362C", 200, 3, 8)

# Eyes
dot_oval(-42, 48, 22, 12, "#FFFFFF", 60, 3, 6)
dot_oval(42, 48, 22, 12, "#FFFFFF", 60, 3, 6)
dot_oval(-42, 48, 8, 9, "#30251F", 25, 4, 7)
dot_oval(42, 48, 8, 9, "#30251F", 25, 4, 7)

# Eyebrows
dot_oval(-42, 75, 25, 7, "#30251F", 60, 3, 7)
dot_oval(42, 75, 25, 7, "#30251F", 60, 3, 7)

# Nose
dot_oval(0, 5, 15, 28, "#D69B72", 90, 3, 7)
dot_oval(0, -12, 17, 8, "#C88E6B", 45, 3, 6)

# Mouth
dot_oval(0, -48, 28, 6, "#2B1D18", 50, 3, 6)

# Beard detail around mouth
dot_oval(-30, -48, 15, 13, "#49362C", 70, 3, 7)
dot_oval(30, -48, 15, 13, "#49362C", 70, 3, 7)

# More hair texture
dot_oval(0, 165, 70, 25, "#49362C", 100, 3, 7)

screen.mainloop()