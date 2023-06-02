# paddle = Turtle()
# paddle.shape('square')
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.color('white')
# paddle.penup()
# paddle.goto(350,0)


from turtle import Turtle

def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)

class Paddle(Turtle):

    def __init__(self, pos1, pos2):
        super().__init__()
        paddle = Turtle()
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos1,pos2)


