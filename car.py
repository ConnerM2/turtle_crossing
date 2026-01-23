from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        rand_y = random.randint(-100, 100) #Gives random y cord
        self.penup()
        self.setheading(180)
        self.teleport(300, rand_y)
        self.shape('square')

    def move(self):
        self.forward(20)
