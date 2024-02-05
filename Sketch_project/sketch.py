# Importing the turtle library
from turtle import Turtle, Screen

# tim instance and screen instance
tim = Turtle()
screen = Screen()


# functions to move forwards
def forwards():
    tim.forward(30)


# functions to move backwards
def backwards():
    tim.backward(30)


# functions to rotate anti-clockwise
def anti_clockwise():
    total = tim.heading() + 10
    tim.setheading(total)


# functions to rotate clockwise
def clockwise():
    total = tim.heading() - 10
    tim.setheading(total)


# functions to clear the screen
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# To listen the event handler
screen.listen()
# Using key to move forwards, backwards, anti-clockwise, clockwise
screen.onkey(forwards, "a")
screen.onkey(backwards, "s")
screen.onkey(anti_clockwise, "d")
screen.onkey(clockwise, "z")
screen.onkey(clear, "c")
# To exit the screen after click
screen.exitonclick()
