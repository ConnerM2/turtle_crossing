from turtle import Screen
from player import Player
from car import Car
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
car = Car()
scoreboard = ScoreBoard()
last_time = time.time()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


gameOn = True

while gameOn:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        scoreboard.update(player)
        car.increase_speed()
        print(car.speed)

    car.create_cars()
    car.move()

    for vehicle in car.all_cars:
        if player.distance(vehicle) < 20:
            gameOn = False

screen.exitonclick()