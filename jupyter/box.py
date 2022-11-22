from turtle import *

def draw_box(x, y, side, color):   
    """x, y - the origin of the box to draw at lower left corner
    side - the length of the side of the box
    color - fill color for the box """
    Turtle()
    penup()
    goto(x,y)
    pendown()
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(side)
        left(90)
    end_fill()
