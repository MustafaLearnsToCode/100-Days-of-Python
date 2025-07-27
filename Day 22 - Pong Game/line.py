from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,300)
        self.setheading(270)
        self.pensize(width=2)
        self.speed(0)

    def dashed(self):
        for i in range(25):
            for c in ('white', 'black'):
                self.color(c)
                self.forward(10)
