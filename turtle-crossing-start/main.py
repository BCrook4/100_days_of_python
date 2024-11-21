import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move_car()
    car.generate_car()

    screen.listen()
    screen.onkeypress(player.move_up, "Up")

    if player.ycor() > 290:
        player.reset_player()
        scoreboard.update_score()
        car.speed_up()

    for i in car.cars:
        if player.distance(i) < 23:
            scoreboard.game_over()
            game_is_on = False







screen.exitonclick()