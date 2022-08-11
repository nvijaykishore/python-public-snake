from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
numb = 0

snake = Snake()
food = Food()
food1 = Food()

scb = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
scb.write_score(0)

while is_game_on:

    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(col="green")
        snake.extend()
        numb += 1
        scb.write_score(num=numb)

    if snake.head.distance(food1) < 15:
        food1.refresh(col="pink")
        snake.extend()
        numb += 1
        scb.write_score(num=numb)

    # Detect collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scb.game_over()

    # Detect collision with tail -collides with any segment in the tail

    # for segment in snake.segments:
    #     if snake.head == segment:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         scb.game_over()

    # using slicing
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scb.game_over()


screen.exitonclick()
