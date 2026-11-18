from turtle import Screen

import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()


tim.speed("fastest")
tim.penup()
tim.hideturtle()
size = 20
color_list = [(152, 72, 51), (210, 147, 106), (47, 28, 18), (238, 217, 190), (201, 93, 80), (242, 209, 97), (174, 51, 58), (136, 36, 23), (209, 79, 85), (119, 172, 196)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.pencolor(random.choice(color_list))
    tim.dot(size, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen= turtle_module.Screen()
screen.exitonclick()