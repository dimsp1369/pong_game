from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.player_1 = 0
        self.player_2 = 0
        self.upd_score()

    def upd_score(self):
        self.clear()
        self.goto(-50, 240)
        self.write(f"{self.player_1}", align="center", move=True, font=('Atial', 24, 'normal'))
        self.goto(50, 240)
        self.write(f"{self.player_2}", align="center", move=True, font=('Atial', 24, 'normal'))

    def player_1_ball(self):
        self.player_1 += 1
        self.upd_score()

    def player_2_ball(self):
        self.player_2 += 1
        self.upd_score()
