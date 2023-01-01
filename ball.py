from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.bounce = "bottom"
        self.paddle = "right"
        self.out = False
        self.x_cor = 10
        self.y_cor = 10

    def move(self, ):
        new_x = self.xcor() + self.x_cor if self.paddle == "left" else self.xcor() - self.x_cor
        new_y = self.ycor() + self.y_cor if self.bounce == "bottom" else self.ycor() - self.y_cor
        self.goto(new_x, new_y)

    def vector(self, new):
        self.bounce = new

    def hitted_to(self, current):
        self.paddle = current

    def set_out(self, bool):
        self.out = bool

    def speed(self):
        self.x_cor += 1
        self.y_cor += 1
