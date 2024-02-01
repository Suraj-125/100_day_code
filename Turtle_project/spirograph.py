# TODO : Create a Spirograph

import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
rgb_color = []

for _ in range(100):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    rgb_color.append(rgb)


def spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random.choice(rgb_color))
        tim.circle(100)
        tim.setheading(tim.heading() + size)


tim.speed("fastest")
spirograph(1)

screen = turtle.Screen()
screen.exitonclick()
