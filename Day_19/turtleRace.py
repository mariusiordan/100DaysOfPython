from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
print(f"user bet is: {user_bet}")

colors = ["red", "blue", "green", "tomato", "purple", "cyan", "pink"]
y_positions = [150, 100, 50, 0, -50, -100, -150]
all_turtles = []

for turtle_index in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"{winning_color} wins!")
            else:
                print(f"{winning_color} loses!")

        random_distance = random.randint(0, 12)
        turtle.forward(random_distance)




screen.exitonclick()