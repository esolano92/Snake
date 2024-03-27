from turtle import Turtle, Screen
X_Y_CORDINATES = [(0,0),(-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        
        
    def create_snake(self):
        for x_y in X_Y_CORDINATES:
            self.add_square(x_y)
            
    
    def extend(self):
        self.add_square(self.squares[-1].position())
        
    def add_square(self, x_y):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        self.squares.append(square)
        square.goto(x_y)
        
    def move(self):
        for squares_num in range(len(self.squares)- 1,0,-1):
            new_x = self.squares[squares_num -1].xcor()
            new_y = self.squares[squares_num -1].ycor()
            self.squares[squares_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
