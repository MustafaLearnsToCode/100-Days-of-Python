from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
timmy = Turtle()

game_started = False
message_cleared = False

def start_game():
    global game_started
    game_started = True

screen.listen()
screen.onkey(lambda: (start_game(), snake.up()), "w")
screen.onkey(lambda: (start_game(), snake.down()), "s")
screen.onkey(lambda: (start_game(), snake.left()), "a")
screen.onkey(lambda: (start_game(), snake.right()), "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    if not game_started:
        timmy.color("white")
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(0, -100)
        timmy.write("Press arrow key to start", align="center", font=("Courier", 20, "normal"))

    if game_started and not message_cleared:
        timmy.clear()
        message_cleared = True

    if game_started:
        snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.final_score_clear()
            scoreboard.game_over()
            scoreboard.final_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.final_score_clear()
        scoreboard.game_over()
        scoreboard.final_score()





















screen.exitonclick()