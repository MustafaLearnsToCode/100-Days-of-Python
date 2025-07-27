import colorgram
from turtle import Turtle,Screen,colormode
import random
from ascii import logo

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(204, 164, 107), (151, 73, 47), (239, 245, 240), (234, 237, 242), (52, 93, 125), (222, 202, 136), (169, 153, 41), (137, 31, 22), (132, 162, 185), (200, 91, 70), (48, 122, 88), (65, 47, 41), (14, 101, 73), (147, 178, 147), (235, 175, 165), (162, 142, 157), (109, 73, 77), (18, 85, 89), (184, 205, 173), (56, 46, 49), (149, 18, 22), (38, 61, 75), (49, 65, 80), (86, 145, 129), (184, 86, 89), (109, 126, 151), (178, 191, 209), (218, 176, 181)]

def painting(dots_col, dots_row, dot_size, spacing):
    timmy = Turtle()
    timmy.shape("circle")
    timmy.hideturtle()
    timmy.penup()
    colormode(255)

    screen = Screen()

    start_x = -(dots_col * spacing) // 2
    start_y = -(dots_row * spacing) // 2
    timmy.goto(start_x, start_y)
    for row in range(dots_row):
        for col in range(dots_col):
            timmy.speed(0)
            timmy.dot(dot_size, random.choice(color_list))
            if col < dots_col - 1:
                timmy.forward(spacing)
        if row < dots_row - 1:
            timmy.speed(0)
            timmy.goto(start_x, start_y + (row + 1) * spacing)

    return screen

print(logo)

print("Welcome to the Dot Painting Simulator!")
dots_col_q = int(input("How many dots per row?: "))
dots_row_q = int(input("How many rows?: "))
dot_size_q = int(input("Dot size in pixels?: "))
spacing_q = int(input("Spacing between dots?: "))

print("\nCreating your painting...The GUI will open shortly!")

painting(dots_col=dots_col_q, dots_row=dots_row_q, dot_size=dot_size_q, spacing=spacing_q)

print("\nEnjoy your painting!\n(p.s. you can click the popup to close it)")

Screen().exitonclick()