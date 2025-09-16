from pico2d import *
import math

open_canvas(800, 600)

boy = load_image('character.png')
grass = load_image('grass.png')

# 1. 경로 데이터 정의
rectangle_points = [(20, 90), (780, 90), (780, 560), (20, 560), (20, 90)]
# 2. 삼각형 경로 수정 (오른쪽으로 먼저 가도록 순서 변경)
triangle_points = [(400, 90), (780, 90), (400, 560), (20, 90), (400, 90)]

# 3. 경로 순서에 원 추가
paths = {
    'rectangle': rectangle_points,
    'triangle': triangle_points,
    'circle': []
}
path_order = ['rectangle', 'triangle', 'circle']

# 캐릭터 상태 변수
x, y = 20, 90
speed = 300

# 경로 추적 변수
path_index = 0
target_index = 1
current_path_name = path_order[path_index]
target_x, target_y = paths[current_path_name][target_index]

# 원 운동 변수
circle_angle = 0

running = True
last_time = 0.0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False


def update(frame_time):
    global x, y, target_x, target_y, target_index, path_index, current_path_name, circle_angle

    if current_path_name == 'circle':
        cx, cy, r = 400, 325, 235
        # 1초에 180도씩 회전
        circle_angle += 180 * frame_time

        if circle_angle >= 360:
            circle_angle = 0
            path_index = (path_index + 1) % len(path_order)
            current_path_name = path_order[path_index]
            target_index = 1
            x, y = paths[current_path_name][0]
            target_x, target_y = paths[current_path_name][target_index]

        x = cx + math.cos(math.radians(circle_angle - 90)) * r
        y = cy + math.sin(math.radians(circle_angle - 90)) * r
    else:
        dx, dy = target_x - x, target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        move_dist = speed * frame_time
        if distance < move_dist:
            x, y = target_x, target_y
            target_index += 1
            if target_index >= len(paths[current_path_name]):
                path_index = (path_index + 1) % len(path_order)
                current_path_name = path_order[path_index]
                if current_path_name == 'circle':
                    circle_angle = 0
                    return

                target_index = 1
                x, y = paths[current_path_name][0]

            target_x, target_y = paths[current_path_name][target_index]
        else:
            x += move_dist * dx / distance
            y += move_dist * dy / distance


def draw():
    clear_canvas()
    grass.draw(400, 30)
    boy.draw(x, y)
    update_canvas()


# --- 메인 루프 ---
while running:
    current_time = get_time()
    frame_time = current_time - last_time
    last_time = current_time

    handle_events()
    update(frame_time)
    draw()

close_canvas()