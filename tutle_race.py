from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput("Make your Bet", "Enter your color")
is_race_on = False

color = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [175, 105, 35, -35, -105, -175]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} tutle is the winner!")
            else:
                print(f"You've lost! The {winning_color} tutle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)

s.exitonclick()
