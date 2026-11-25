from turtle import Turtle

STARTING_POSITION_PLAYER1 = [(-630, 0), (-630, 20), (-630, -20)]
STARTING_POSITION_PLAYER2 = [(630, 0), (630, 20), (630, -20)]

class Paddle():
    def __init__(self):
        self.segments = []
        self.create_paddle(STARTING_POSITION_PLAYER1)
        self.create_paddle(STARTING_POSITION_PLAYER2)




    def create_paddle(self, position):
        for segments in position:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
