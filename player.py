from turtle import Turtle 
from car_manager import CarManager

MOVE_INCREMENT = 10

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.speed(0)
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # def reset_game(self):
    #     if self.ycor() == FINISH_LINE_Y:
    #         self.hideturtle()
    #         self.showturtle()