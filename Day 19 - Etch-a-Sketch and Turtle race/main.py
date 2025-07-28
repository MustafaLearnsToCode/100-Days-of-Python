import turtle
from turtle import Turtle,Screen
import random
from tkinter import messagebox
import tkinter as tk

screen = Screen()
timmy = Turtle()
timmy.speed(10)
# def move_forwards():
#     timmy.forward(10)
# def move_backwards():
#     timmy.back(10)
# def rotate_clockwise():
#     timmy.right(5)
# def rotate_anticlockwise():
#     timmy.left(5)
# def clear():
#     timmy.reset()
#
# screen.listen()
# screen.onkey(fun=move_forwards, key="w")
# screen.onkey(fun=move_backwards, key="s")
# screen.onkey(fun=rotate_clockwise, key="d")
# screen.onkey(fun=rotate_anticlockwise, key="a")
# screen.onkey(fun=clear, key="c")

def result(title, message):
    messagebox.showinfo(title, message)

race_start = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =  []

y_axis = 0
for i in colors:
    i_timmy = Turtle("turtle")
    i_timmy.color(i)
    i_timmy.penup()
    i_timmy.goto(x=-230, y=-90+y_axis)
    y_axis += 30
    all_turtles.append(i_timmy)

if user_bet:
    race_start = True

while race_start:
    for i in all_turtles:
        if i.xcor() > 220:
            race_start = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                # print(f"You won! The {winning_color} turtle is the winner!")
                result(title="",message=f"You Won!\nThe {winning_color} turtle is the winner!" )
            else:
                # print(f"You lost...The {winning_color} turtle is the winner!")
                result(title="", message=f"You Lost...\nThe {winning_color} turtle is the winner!")
            break

        random_dist = random.randint(0,10)
        i.forward(random_dist)


screen.exitonclick()