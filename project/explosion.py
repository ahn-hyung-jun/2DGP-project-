from pico2d import *
import math
import game_world
import game_framework

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Explosion:
    image = None

    def __init__(self, x = 400, y = 300):
        if Explosion.image == None:
            self.image = load_image('explosion.png')
        self.frame = 0
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_composite_draw(0 + int(self.frame)*180, 180, 180, 180, 0, '', self.x, self.y, 100, 100)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.frame > 7:
            game_world.remove_object(self)




