from turtle import Turtle

class Finish(Turtle):

    def __init__(self, screen_width = 600):
        super().__init__()
        self.screen_width = screen_width
        self.speed(0)
        self.penup()
        self.hideturtle()

    def draw_finish_line(self, y_position=300):
        square_size = 10
        num_squares = self.screen_width // square_size
        start_x = -self.screen_width // 2

        for row in range(2):
            for col in range(num_squares):
                x = start_x + col * square_size
                y = y_position - (row * square_size)

                self.goto(x, y)

                if (row + col) % 2 == 0:
                    self.color("black", "black")
                else:
                    self.color("white", "white")

                self.pendown()
                self.begin_fill()
                for _ in range(4):
                    self.forward(square_size)
                    self.right(90)
                self.end_fill()
                self.penup()