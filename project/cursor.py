from pico2d import *
import math
import game_world
import game_framework
import main_state

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Cursor:
    image = None

    def __init__(self):
        self.image = load_image('mouse.png')
        self.x = 0
        self.y = 0
        global mouse_x, mouse_y
        mouse_x = 0
        mouse_y = 0

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x = mouse_x
        self.y = mouse_y

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            global mouse_x, mouse_y
            mouse_x, mouse_y = event.x, 1024 - event.y




