from pico2d import *
import random

open_canvas(800,800)

class ball():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100,900) , 599
        self.size = random.randint(20,80)
        self.yspeed = 0
        self.gravity = random.uniform(0.1,2.0)
        self.onGround = False

    def update(self):
        if self.y > self.size / 2:
            self.yspeed -= self.gravity
            self.y += self.yspeed
        else:
            self.y = self.size / 2
            self.onGround = True

    def render(self):
        self.image.draw(self.x, self.y,self.size,self.size)

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
balls = [ball() for _ in range(20)]

while running:
    handle_events()
    clear_canvas()
    for ball in balls:
        if ball.onGround is False:
            ball.update()
        ball.render()
    update_canvas()
    delay(0.016)

close_canvas()