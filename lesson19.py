#event listeners
#object states

from turtle import Turtle, Screen
import random

red = Turtle()
green = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = scren.textinput(title='Make a bet.', prompt='Which color will win the race?')

screen.exitonclick()
red.goto(x=-250, y=0)
green.goto(x=-250, y=-30)

red.setheading(90)
green.setheading(90)

def rand_int():
    ranndnum = random.randint(1,10)
    return ranndnum

def go():
    red.forward(rand_int())
    green.forward(rand_int())

while int(red.xcor) or int(green.xcor) < 180:
    go()
