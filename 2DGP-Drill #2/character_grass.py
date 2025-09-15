from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

gab = 90
x = 400
y = gab
state = 0
square = True
radian = 0
speed = 20

def move_square():
    global  x,y,state,square
    if (state == 0):
        x = x + speed
        if(x >= 800 - gab / 5):
            x = 800- gab / 5
            state = 1
    elif (state == 1):
        y = y + speed
        if(y >= 600- gab/1.5):
            y = 600- gab/1.5
            state = 2
    elif (state == 2):
        x = x - speed
        if(x <= 0+ gab / 5):
            x = 0+ gab / 5
            state = 3
    elif (state == 3):
        y = y - speed
        if(y <= 0+ gab):
            y = 0+ gab
            state = 4
    elif (state == 4):
        x = x+speed
        if(x >= 400):
            x = 400
            state = 0
            square = False


def move_circle():
    global x, y, square, radian

    x = math.cos(radian - math.pi / 2) * 250 + 400
    y = math.sin(radian - math.pi / 2) * 250 + 330
    radian += 0.075 * 2

    if radian >= 2 * math.pi:
        square = True
        radian = 0
        state = 0
        x = 400
        y = gab


while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)

    if(square):
        move_square()
    else:
        move_circle()

    character.draw_now(x, y + 9)
    delay(0.01)

