from turtle import Turtle, Screen
from lesson22_paddles import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
#screenrefresh for no animation
screen.tracer(0)

rpaddle = Paddle([350,0])
lpaddle = Paddle([350,0])

screen.listen()
screen.onkey(rpaddle.go_up, 'Up')
screen.onkey(rpaddle.go_down, 'Down')

game_on = True
while game_on:
    screen.update()



screen.exitonclick()