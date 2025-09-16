from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def render(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.016)


def move_rectangle():
    print('Moving rectangle')
    render(400,300)
    pass


def move_circle():
    print('Moving circle')
    for angle in range(0,360,1):
        x = 400 + math.cos(math.radians(angle)) * 280
        y = 300 + math.sin(math.radians(angle)) * 280
        render(x,y)
    pass


while(True):
    move_rectangle()
    move_circle()