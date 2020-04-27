import turtle
from random import randint as r
Corona = turtle.Turtle()
Corona.down()
while True:
    Corona.forward(r(1,30))
    turn = r(1,3)
    if turn == 1:
        Corona.left(90)
    elif turn == 3:
        Corona.right(90)
    colour = ''
    for i in range(6):
        col = r(0,15)
        if col > 9:
            col = str(col)[1]
            col = chr(ord(col)+17)
        else:
            col = str(col)
        colour += col
    Corona.pencolor('#'+colour)
    Corona.pensize(r(1,10))
