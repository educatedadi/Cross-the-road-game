from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINAL_LINE_Y = (0, 280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.speed(0)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)
