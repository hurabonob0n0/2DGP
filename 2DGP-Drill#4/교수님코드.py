from pico2d import *

animation_datas = [
    {'sheet': load_image('Attack1L.png'), 'frames': 14, 'w': 207, 'h': 237},
    {'sheet': load_image('Attack2L.png'), 'frames': 18, 'w': 343, 'h': 287},
    {'sheet': load_image('Attack3L.png'), 'frames': 15, 'w': 413, 'h': 364},
    {'sheet': load_image('Attack4L.png'), 'frames': 11, 'w': 575, 'h': 445}
]

open_canvas()
sprite = load_image('Attack1L.png')


def Play_Animation():
    pass


while True:
    for i in range(5):
        for animation in animation_datas:
            Play_Animation()
            delay(1)

close_canvas()