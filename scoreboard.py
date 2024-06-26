from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.update_scoreboard
        self.hideturtle()
        self.penup()
        self.goto(0,270)
    
    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)
        
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
