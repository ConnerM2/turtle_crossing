from turtle import Turtle



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.teleport(0, -280)
        self.setheading(90)
        self.shape('turtle')
        self.SPEED = 20

    def move(self):
        self.forward(self.SPEED)

    def  move_up(self):
        self.setheading(90)
        self.move()

    def move_down(self):
        self.setheading(270)
        if self.ycor() > -280:
            self.move()

    def reset(self):
        self.setheading(90)
        self.teleport(0,-280)
