from turtle import Turtle, Screen
from lesson22_paddles import Paddle
from lesson22_ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
#screenrefresh for no animation
screen.tracer(0)

rpaddle = Paddle([350,0])
lpaddle = Paddle([350,0])
ball = Ball()

screen.listen()
screen.onkey(rpaddle.go_up, 'Up')
screen.onkey(rpaddle.go_down, 'Down')
screen.onkey(lpaddle.go_up, 'w')
screen.onkey(lpaddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(0.2)
    screen.update()
    ball.move()

    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce()

    #collisionwith paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 340:
        ball.paddlebounce()
    
    if ball.distance(lpaddle) < 50 and ball.xcor() > -340:
        ball.paddlebounce()



screen.exitonclick()