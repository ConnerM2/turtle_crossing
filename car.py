from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = 10
        self.ran_num = 6

    def create_cars(self):
        random_chance = random.randint(1, self.ran_num)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            ran_y = random.randint(-250, 250)
            new_car.teleport(300, ran_y)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.speed += 5
        self.ran_num -= 1

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def delete(self):
        if self.xcor() < -300:
            self.delete()
