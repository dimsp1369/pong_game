from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, auto=False):
        super().__init__()
        self.auto = auto
        self.is_bottom_edge = True
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1, 1)
        self.paddle_position()

    def up(self):
        if self.ycor() < 250:
            new_move = self.ycor() + 20
            self.sety(new_move)

    def down(self):
        if self.ycor() > -240:
            new_move = self.ycor() - 20
            self.sety(new_move)

    def paddle_position(self):
        if self.auto == True:
            self.goto(360, 0)
        else:
            self.goto(-370, 0)

    def auto_move(self):
        if self.is_bottom_edge:
            if self.ycor() < 250:
                new_move = self.ycor() + 15
                self.sety(new_move)
            else:
                self.is_bottom_edge = False
        elif not self.is_bottom_edge:
            if self.ycor() > -240:
                new_move = self.ycor() - 15
                self.sety(new_move)
            else:
                self.is_bottom_edge = True
