import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()

rgb_colors = [ (244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()