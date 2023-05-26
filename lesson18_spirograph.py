
import random
from turtle import Turtle, Screen

timmy = Turtle()

# def random_color():
#   r = random.randint(1,255)
#   g = random.randint(1,255)
#   b = random.randint(1,255)
#   color = (r,g,b)
#   return color
colors = ['red', 'blue', 'green']


timmy.speed('fastest')

for x in range(50):
    new_color = random.choice(colors)
    timmy.color(new_color)
    timmy.circle(50)
    # timmy.right(3)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)


screen = Screen()
screen.colormode(255)
screen.exitonclick()