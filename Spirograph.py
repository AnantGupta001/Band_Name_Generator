from turtle import Turtle, Screen
import random

s = Screen()
t = Turtle()

s.colormode(255)
t.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def make_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_colour())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


make_circle(5)
s.exitonclick()
