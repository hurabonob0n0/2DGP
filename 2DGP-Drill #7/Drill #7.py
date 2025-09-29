from pico2d import *
import random

open_canvas(400,800)

class ball():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100,300) , 599

    def updaate(self):
        pass

    def render(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN: # 키가 눌렸을 때
            if event.key == SDLK_ESCAPE:
                running = False

running = True
balls = [ball() for _ in range(5)]

while running:
    handle_events()
    clear_canvas()
    for ball in balls:
        ball.render()
    update_canvas()
    delay(0.016)

close_canvas()