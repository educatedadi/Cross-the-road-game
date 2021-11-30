from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
loop_count = 0
car_on_frame = 6
game_is_on = True
while game_is_on:
    screen.update()
    screen.onkey(key='Up', fun=player.move_forward)
    if loop_count % car_on_frame == 0:
        car_manager.create_car()
    car_manager.move_car()

    collision_happened = car_manager.detect_collision(player)
    if collision_happened:
        scoreboard.game_over()
        game_is_on = False

    if player.ycor() > 280:
        player.level_up()
        scoreboard.level_up()
        car_manager.level_up()
        car_on_frame -= 1

    loop_count += 1
    time.sleep(0.1)

screen.exitonclick()
