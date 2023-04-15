from turtle import Turtle as t
import random

ani = t()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def drawshape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        ani.fd(100)
        ani.right(angle)

for shape_side_n in range(3,11):
    ani.color(random.choice(colors))
    drawshape(shape_side_n)



