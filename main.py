from turtle import Turtle, Screen
from player import Player
from car import Car
import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
car1 = Car()

def gen_car():
    new_car = Car()
    return new_car


gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    car1.move()

screen.exitonclick()