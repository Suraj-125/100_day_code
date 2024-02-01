# TODO : Creating an Hist

# Importing libraries
import turtle
import random
import colorgram

# Extracting 30 unique rgb colors from image.jpg
colors = colorgram.extract("image.jpg", 30)

# Creating an empty list to store the tuple of rgb colors
rgb_color = []
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb = (red, green, blue)
    rgb_color.append(rgb)

# Creating instance of Turtle
tim = turtle.Turtle()

# Setting for rgb mode
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

total_dot = 100

# Looping the total_dot for 100 times
for each_dot in range(1, total_dot + 1):
    tim.dot(20, random.choice(rgb_color))
    tim.forward(50)

    if each_dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Hiding the turtle at last
tim.hideturtle()

# Creating screen instance to visualise the gui
screen = turtle.Screen()

# This will hold the screen
screen.exitonclick()