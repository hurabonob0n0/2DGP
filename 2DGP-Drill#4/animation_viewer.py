from pico2d import *

open_canvas()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
MAX_REPEATS = 5
PAUSE_FRAMES = 25

animation_data = []
current_animation = 0
frame_index = 0
repeat_count = 0
pause_counter = 0

def load_resources():
    global animation_data
    animation_data = [
        {'sheet': load_image('Attack1L.png'), 'frames': 14, 'w': 207, 'h': 237},
        {'sheet': load_image('Attack2L.png'), 'frames': 18, 'w': 343, 'h': 287},
        {'sheet': load_image('Attack3L.png'), 'frames': 15, 'w': 413, 'h': 364},
        {'sheet': load_image('Attack4L.png'), 'frames': 11, 'w': 575, 'h': 445}
    ]

def update():
    global pause_counter, current_animation, frame_index, repeat_count

    if pause_counter > 0:
        pause_counter -= 1
        if pause_counter == 0:
            current_animation = (current_animation + 1) % len(animation_data)
            frame_index = 0
            repeat_count = 0
    else:
        anim_info = animation_data[current_animation]
        frame_index = (frame_index + 1) % anim_info['frames']

        if frame_index == 0:
            repeat_count += 1
            if repeat_count >= MAX_REPEATS:
                pause_counter = PAUSE_FRAMES

def render():
    global current_animation,animation_data
    clear_canvas_now()
    anim = animation_data[current_animation]
    sheet = anim['sheet']
    frame_w, frame_h = anim['w'], anim['h']
    clip_l = frame_index * frame_w

    scale_ratio = (CANVAS_HEIGHT // 2) / frame_h * 1.5
    draw_w, draw_h = int(frame_w * scale_ratio), int(frame_h * scale_ratio)

    sheet.clip_draw(clip_l, 0, frame_w, frame_h,
                    CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, draw_w, draw_h)

    update_canvas()
    delay(0.04)



load_resources()

while(True):
    update()
    render()

