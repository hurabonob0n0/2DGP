from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')


def move_rectangle():
    print('Moving rectangle')
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass


def move_circle():
    print('Moving circle')
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass


while(True):
    move_rectangle()
    move_circle()