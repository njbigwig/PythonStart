from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.clear()
        self.goto(-280, 265)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="left", font=FONT)
        
        
        

