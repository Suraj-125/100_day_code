# Importinf the module
import turtle as t
import random

# Creating instance of turtle class
tim = t.Turtle()
t.colormode(255)

# Empty list to store tuple of rgb color
rgb_color = []

# Looping the color for rgb
for color in range(100):
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    rgb_color.append(rgb)

# Allocating the turtle to the starting position
tim.shape("turtle")
tim.penup()
tim.speed("fastest")
tim.setheading(220)
tim.forward(465)
tim.setheading(90)

# Looping for the required dot
for dot in range(1, 481):
    tim.dot(20, random.choice(rgb_color))
    tim.forward(31)

    if dot % 20 == 0:
        tim.setheading(0)
        tim.forward(31)
        tim.setheading(270)
        tim.forward(620)
        tim.setheading(90)

# Hiding the turtle
tim.hideturtle()

# Initializing the gui of turtle screen
screen = t.Screen()
screen.exitonclick()



