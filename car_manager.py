from turtle import Turtle
import random

COLORS = ['red', 'orange', 'green', 'purple', 'blue', 'yellow']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.create_car()

    def create_car(self):
        car_object = Turtle()
        car_object.penup()
        car_object.setx(300)
        car_object.sety(random.randint(-230, 250))
        car_object.shape('square')
        car_object.color(random.choice(COLORS))
        car_object.shapesize(1, 2)
        car_object.setheading(180)
        self.car_list.append(car_object)

    def move_car(self):
        for car in self.car_list:
            if car.xcor() > -320:
                car.forward(self.move_distance)
            else:
                self.car_list.remove(car)

    def detect_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:
                return True

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

