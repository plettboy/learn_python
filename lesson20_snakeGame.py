from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer()

segments = []

starting_position = [(0,0), (-20,0), (-40,0)]
for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
    screen.update()
 
screen.listen()
screen.onkey('Down')
screen.onkey('Up')
screen.onkey('Left')
screen.onkey('Right')

game_on = True
while game_on:
    for seg in segments():
        seg.forward(20)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
# segment_1 = Turtle('square')
# segment_1.color('white')

# segment_2 = Turtle('square')
# segment_2.color('white')
# segment_2.goto(-20,0)

# segment_3 = Turtle('square')
# segment_3.color('white')
# segment_3.goto(-40,0)


