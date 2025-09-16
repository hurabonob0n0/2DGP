from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def render(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.008)


def move_bottomR():
    for x in range(400,780,4):
        render(x,40)

def move_bottomL():
    for x in range(20, 400,4):
        render(x, 40)

def move_top():
    for x in range(780, 0,-4):
        render(x, 560)

def move_right():
    for y in range(40, 560,4):
        render(780, y)

def move_left():
    for y in range(560, 40,-4):
        render(20, y)


def move_rectangle():
    print('Moving rectangle')
    move_bottomR()
    move_right()
    move_top()
    move_left()
    move_bottomL()

def move_circle():
    print('Moving circle')
    for angle in range(0,360,2):
        x = 400 + math.cos(math.radians(angle-90)) * 260
        y = 300 + math.sin(math.radians(angle-90)) * 260
        render(x,y)


def move_Right_to_Top_Middle():
    print('Moving right to top-middle')
    x1, y1 = 780, 40
    x2, y2 = 400, 560

    for i in range(0, 100, 2):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        render(x, y)

# 위쪽 중앙 -> 왼쪽 아래
def move_Top_Middle_to_Left():
    print('Moving top-middle to left')
    x1, y1 = 400, 560
    x2, y2 = 20, 40

    for i in range(0, 100, 2):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        render(x, y)


def move_triangle():
    move_bottomR()
    move_Right_to_Top_Middle()
    move_Top_Middle_to_Left()
    move_bottomL()



while(True):
    move_rectangle()
    move_triangle()
    move_circle()