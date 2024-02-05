# importing libraries
import turtle
import random

# creating an instance
tim = turtle.Turtle()

# Using the rgb colormode
turtle.colormode(255)

# Creating an empty list to store the tuple of rgb color
rgb_color = []

# Using for loop for a range of 100 times
for color in range(100):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Generating rgb color
    rgb = (red, green, blue)

    # Appending in the empty list
    rgb_color.append(rgb)

# Shaping to turtle mode
tim.shape("turtle")

# Using penup, not to draw anything
tim.penup()

# Increasing the speed of turtle
tim.speed("fastest")

# CHanging the angle
tim.setheading(135)

# Moving forward
tim.forward(350)
tim.setheading(0)

total = 100

# Looping in a range of 100 times to generate dot
for dot in range(1, total + 1):
    tim.dot(20, random.choice(rgb_color))
    tim.forward(50)

    # if dot divided by 10 gets remainder 0 then
    if dot % 10 == 0:

        # turn downward
        tim.setheading(270)

        # move forward
        tim.forward(50)

        # turn right
        tim.setheading(180)

        # move forward 500
        tim.forward(500)

        # turn backward
        tim.setheading(0)

# Hiding the turtle after completion
tim.hideturtle()

# Creating instance for holding the screen
screen = turtle.Screen()

# It will shut down the screen after clicking it on screen
screen.exitonclick()