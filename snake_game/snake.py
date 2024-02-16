# Steps to create the snake game
# TODO 1: Create a snake body
# TODO 2: Move the snake
# TODO 3: Control the snake using the keyboard
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

# Importing libraries from modules
from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Creating the screen
screen = Screen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")

# Using tracer to stop the square
screen.tracer(0)

# Creating instances
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Initiating the keyboard key for movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# flag
is_game = True

while is_game:
    # Update to start the square in smooth manner
    screen.update()
    # time to sleep the square at specific time
    time.sleep(0.2)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game = False
        scoreboard.game_over()

    # Detect collision with segments
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass

        if snake.head.distance(segment) < 10:
            is_game = False
            scoreboard.game_over()


screen.exitonclick()
