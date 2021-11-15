import random

import colorgram
import turtle


def create_turtle():
    turtle_object = turtle.Turtle()
    turtle_object.pensize(2)
    turtle.colormode(255)
    turtle_object.speed(1000)
    return turtle_object


def get_colors(path):
    rgb_colors = []
    colors = colorgram.extract(path, 50)
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return rgb_colors


def draw_star(turtle_object, color):
    turtle_object.color(color)
    for _ in range(5):
        turtle_object.forward(20)
        turtle_object.right(144)


def change_forward(turtle_object):
    turtle_object.penup()
    turtle_object.setheading(90)
    turtle_object.forward(30)
    turtle_object.setheading(180)
    turtle_object.forward(630)
    turtle_object.setheading(0)
    turtle_object.pendown()


def get_picture(turtle_object, number_of_stars):
    turtle_object.penup()
    tur.setx(-335)
    tur.sety(-305)
    turtle_object.pendown()

    for star_count in range(1, number_of_stars):
        draw_star(turtle_object, random.choice(colors))
        turtle_object.penup()
        turtle_object.forward(30)
        turtle_object.pendown()
        if star_count % 21 == 0:
            draw_star(turtle_object, random.choice(colors))
            change_forward(turtle_object)


colors = get_colors('painting/image.jpg')
tur = create_turtle()
get_picture(tur, 210)
tur.hideturtle()

screen = turtle.Screen()
screen.exitonclick()


