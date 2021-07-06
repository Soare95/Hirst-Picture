import turtl
import random

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58),
       (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173),
       (189, 99, 107), (139, 33, 28),  (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212),
       (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]

timy = turtle.Turtle()
turtle.colormode(255)
timy.hideturtle()
timy.speed(0)

timy.penup()


def dot_line():
    for column in range(10):
        for dot in range(10):
            timy.dot(20, random.choice(color_list))
            timy.penup()
            timy.forward(50)
        timy.setx(0)
        timy.penup()
        timy.left(90)
        timy.forward(50)
        timy.right(90)



dot_line()




screen = turtle.Screen()
screen.exitonclick()
