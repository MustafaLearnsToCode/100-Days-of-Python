from turtle import Turtle,Screen, colormode
import random

timmy = Turtle()
timmy.shape("circle")
timmy.shapesize(0.5)
colormode(255)
timmy.speed("fastest")

for i in range(4):
    timmy.forward(100)
    timmy.left(90)

for i in range(25):
    for c in ('white', 'black'):
        timmy.color(c)
        timmy.forward(5)

for i in range(25):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

def polygons(start_sides, times):
    for i in range(times):
        timmy.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        for i in range(start_sides):
            timmy.forward(50)
            timmy.left(360/start_sides)
        start_sides += 1

polygons(3, 12)

def random_walk(walk):
    direction = [0,90,180,270]
    for i in range(walk):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        timmy.color(color)
        timmy.forward(25)
        timmy.setheading(random.choice(direction))

random_walk(200)

def draw_spirograph(increment):
    direction = 0
    total_rotation = int(360/increment + 1)
    for i in range(total_rotation):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        timmy.color(color)
        timmy.circle(100)
        timmy.setheading(direction)
        direction += increment

draw_spirograph(10)






screen = Screen()
screen.exitonclick()