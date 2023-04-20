from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

s = Screen()
s.listen()
s.setup(width=600, height=600)
s.tracer(0)
s.bgcolor("green")
s.title("My Snake Game")

snake = Snake()
food = Food()
score = Score()

s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Left", fun=snake.left)

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

s.exitonclick()
