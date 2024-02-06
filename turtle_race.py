"""
Turtle Race Game project is created with the help of turtle library. It allows the turtle to race with another opponent
turtle to test themselves who is best amongst them. You can bet your turtle color and enjoy the game.
"""

# importing library
from turtle import Turtle, Screen
import random

# flag
is_game = False

# managing the screen
screen = Screen()
screen.setup(width=500, height=400)

# prompting to bet the turtle
user_bet = screen.textinput(title="Turtle Race", prompt="Bet the colour of your turtle : ")
# print(user_bet)

# initializing list of colors, y_coordinates and an empty all_turtles list
colors = ["red", "green", "blue", "orange", "black", "pink"]
y_coordinate = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# Generating the 6 different colors turtle
for turtle in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle])
    tim.penup()
    tim.goto(x=-230, y=y_coordinate[turtle])
    all_turtles.append(tim)


# print(all_turtles)

# if user_bet is available
if user_bet:
    is_game = True

# If is_game True
while is_game:
    for turtle_speed in all_turtles:
        if turtle_speed.xcor() > 230:
            is_game = False
            winning_color = turtle_speed.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle won the race. Congratulations !")
            else:
                print(f"You {user_bet} turtle lose the race. Winner is {winning_color} turtle.")

        speed = random.randint(0, 10)
        turtle_speed.speed("slowest")
        turtle_speed.forward(speed)

screen.exitonclick()
