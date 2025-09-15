from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

gab = 20
x = 400
y = 9
state = 0
square = True
radian = 0

def move_square():
    global  x,y,state,square
    if (state == 0):
        x = x + 10
        if(x >= 800 - gab):
            x = 800- gab
            state = 1
    elif (state == 1):
        y = y + 10
        if(y >= 600- gab):
            y = 600- gab
            state = 2
    elif (state == 2):
        x = x - 10
        if(x <= 0+ gab):
            x = 0+ gab
            state = 3
    elif (state == 3):
        y = y - 10
        if(y <= 0+ gab):
            y = 0+ gab
            state = 4
    elif (state == 4):
        x = x+10
        if(x >= 400):
            x = 400
            state = 0
            square = False


def move_circle():
    global x,y,state,square,radian

    x = math.cos(radian) * 390 + 400
    y = math.sin(radian) * 290 + 300
    radian += 0.1
    if(radian >= 2*3.14):
        square = True
        radian = 0
        state = 0
        x = 400
        y = 9


while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)

    if(square):
        move_square()
    else:
        move_circle()

    character.draw_now(x, y + 9)
    delay(0.01)

