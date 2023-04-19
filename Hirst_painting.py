from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

s.bgcolor("Beige")
s.colormode(255)

t.speed(0)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

"""
Using this Code, We got color_list 

import colorgram
colors = colorgram.extract('HirstPainting.webp', 30)
def color_extraction():
    """'Returns list of colors from the image "HirstPainting.webp".'"""
    list_of_color = []
    for i in range(30):
        color = colors[i]
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        tuple_of_color = (r, g, b)
        list_of_color.append(tuple_of_color)
    return list_of_color
"""

color_list = [(239, 244, 249), (236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11),
              (108, 179, 218), (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64),
              (17, 28, 175), (213, 135, 176), (9, 185, 214), (205, 29, 142), (229, 168, 197), (125, 189, 162),
              (8, 49, 28), (37, 132, 73), (125, 219, 233), (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201),
              (190, 15, 5), (238, 63, 31)]

for dot_count in range(1, 101):
    t.dot(20, random.choice(color_list))
    t.fd(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(0)
        t.back(500)
        t.setheading(0)

s.exitonclick()
