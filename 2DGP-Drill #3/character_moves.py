from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def render(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.016)


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
    for y in range(20, 560,4):
        render(780, y)

def move_left():
    for y in range(580, 40,-4):
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
    for angle in range(0,360,1):
        x = 400 + math.cos(math.radians(angle-90)) * 280
        y = 300 + math.sin(math.radians(angle-90)) * 280
        render(x,y)

while(True):
    move_rectangle()
    move_circle()