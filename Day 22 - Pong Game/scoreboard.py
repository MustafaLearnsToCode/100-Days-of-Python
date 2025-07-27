from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_end_l_win(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 10)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
        self.goto(0, -20)
        self.write(f"You Lost...by {self.l_score - self.r_score} point(s)", align="center",font=("courier", 20, "normal"))

    def game_end_r_win(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 10)
        self.write("GAME OVER", align="center", font=("courier", 30, "normal"))
        self.goto(0, -20)
        self.write(f"You Won! by {self.r_score - self.l_score} point(s)", align="center",font=("courier", 20, "normal"))



