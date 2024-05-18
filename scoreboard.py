from turtle import Turtle

FONT1 = ("Courier", 20, "normal")
FONT2 = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.up()
        self.goto(-290, 260)
        self.update_scoreboard()

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align= "left", font= FONT1)
        
    def graphic_game_over_box(self):
        self.goto(-150, 50)
        self.pendown()
        self.begin_fill()
        self.color("gray")
        self.forward(300)
        self.right(90)
        self.forward(50)
        self.right(90)
        self.forward(300)
        self.right(90)
        self.forward(50)
        self.end_fill()
        self.penup()
        self.color("black")

    def game_over(self):
        self.graphic_game_over_box()
        self.goto(0, 0)
        self.write("Game Over", align= "center", font= FONT2)