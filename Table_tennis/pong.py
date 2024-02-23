from turtle import Turtle


class Label(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=8)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(350, new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(350, new_y)

    def go_downer(self):
        new_y = self.ycor() - 30
        self.goto(-350, new_y)

    def go_upper(self):
        new_y = self.ycor() + 30
        self.goto(-350, new_y)


