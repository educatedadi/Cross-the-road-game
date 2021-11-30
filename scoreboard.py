from turtle import Turtle

FONT = ('Courier', 24, 'normal')
FONT2 = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.write_level()

    def game_over(self):
        self.home()
        self.write('GAME OVER', False, 'center', FONT)

    def write_level(self):
        self.goto(-230, 270)
        self.clear()
        self.write(f'LEVEL : {self.current_level}', False, 'center', FONT2)

    def level_up(self):
        self.current_level += 1
        self.write_level()
