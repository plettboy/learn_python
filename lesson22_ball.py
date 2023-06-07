from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        newx= self(xcor + 10)
        newy = self(ycor + 10)

    def bounce(self):
        self.y_move *= -1

    def paddlebounce(self):
        self.x_move *= -1