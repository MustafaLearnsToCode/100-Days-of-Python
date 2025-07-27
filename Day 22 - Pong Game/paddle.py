from turtle import Turtle
import random

class Paddle(Turtle):
    
    def __init__(self, position):
     super().__init__()
     self.color("white")
     self.shape("square")
     self.shapesize(stretch_wid=5, stretch_len=1)
     self.penup()
     self.goto(position)
     self.move_amount = 20
     self.max_amount = 50
     self.follow_move = 15

    def paddle_up(self):
         new_y = self.ycor() + self.move_amount
         self.goto(self.xcor(), new_y)

         if self.move_amount < self.max_amount:
             self.move_amount += 5

    def paddle_down(self):
         new_y = self.ycor() - self.move_amount
         self.goto(self.xcor(), new_y)

         if self.move_amount < self.max_amount:
             self.move_amount += 5

    def update_movement(self):
        if self.move_amount > 20:
            self.move_amount -= 1
            if self.move_amount < 20:
                self.move_amount = 20

    def reset_movement(self):
        self.move_amount = 20

    def follow_ball(self, ball):
        if random.randint(0,10) > 1:
            if self.ycor() < ball.ycor() - 10:
                new_y = self.ycor() + self.follow_move
                self.goto(self.xcor(), new_y)
            if self.ycor() > ball.ycor():
                new_y = self.ycor() - self.follow_move
                self.goto(self.xcor(), new_y)

        