from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')


def move_top():
    pass

def move_right():
    pass


def move_bottom():
    pass


def move_left():
    pass


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_circle():
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg))
        y = r * math.sin(math.radians(deg))
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)


while(True):
    move_rectangle()
    move_circle()