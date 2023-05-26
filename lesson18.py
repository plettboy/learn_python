from turtle import Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(45)


screen = Screen()
screen.exitonclick()

timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
for x in range(100)
timmy_the_turtle.forward(2)
timmy_the_turtle.penup()
timmy_the_turtle.forward(2)
timmy_the_turtle.pendown()

import random
colors = ['red', 'green', 'blue']
directions = [0, 90, 180, 270]


def random_color():
    r = random.int(1,255)
    g = random.int(1,255)
    b = random.int(1,255)
    randomcolor = (r, g,  b)
    return random_color

random_color()

for x in range(100):
    timmy_the_turtle.forward(random.randint(1,50))
    new_color = colors.choice()
    new_direction = directions.choice()
    timmy_the_turtle.color(new_color)
    timmy_the_turtle.angle(new_direction)