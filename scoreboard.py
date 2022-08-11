from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pendown()
        self.goto(0,280)
        self.hideturtle()

        # str num = '0'

    def write_score(self, num):
        self.clear()
        self.score = num
        self.color("white")
        self.write(f"Score = {self.score}", False, align="center",font=('Arial', 10, 'normal'))

    def game_over(self):
        size = 0
        self.goto(0,0)
        for n in range(3):
            size += 20
            self.clear()
            time.sleep(0.5)
            self.write("GAME OVER", False, align="center", font=('Arial', size, 'normal'))



