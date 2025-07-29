import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finish_line import Finish

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossy Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
finish_line = Finish()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    finish_line.draw_finish_line()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect player crossed
    if player.at_end():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()


screen.exitonclick()