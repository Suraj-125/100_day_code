# TODO : Create an Angle

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


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


tim.setheading(90)
tim.penup()
tim.forward(200)
tim.setheading(0)
tim.pendown()
tim.pensize(5)
tim.speed("fastest")
for side in range(3, 11):
    tim.color(random.choice(rgb_color))
    draw_shape(side)


screen = turtle.Screen()
screen.exitonclick()
