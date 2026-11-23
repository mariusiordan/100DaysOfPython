from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("carrot")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
