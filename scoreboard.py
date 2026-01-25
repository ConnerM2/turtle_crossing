from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.teleport(-280, 260)
        self.write(f"Level: {self.score}", font=('Arial', 20, 'normal'))

    def update (self, player):
        self.clear()
        player.reset()
        self.score += 1
        self.write(f"Level: {self.score}", font=('Arial', 20, 'normal'))

