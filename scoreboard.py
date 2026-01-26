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

    def game_over(self):
        self.teleport(-75,50)
        self.clear()
        self.write(f"GAME OVER", font=('Arial', 20, 'normal'))

    def final_score(self):
        self.teleport(-60, 0)
        self.write(f"SCORE: {self.score}", font=('Arial', 20, 'normal'))