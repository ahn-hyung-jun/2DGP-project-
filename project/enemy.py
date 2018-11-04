from pico2d import *
import math
import random

from bullet import Bullet
import game_world
import hero



# Hero Run Speed
PIXEL_PER_METER =  (1.0/0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

# Hero Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Enemy:
    def __init__(self):
        self.hp = 100
        self.x , self.y  = 400,300
        self.fire_timer = 1000
        self.fire_speed = 10
        self.image = load_image('hero_sprite.png')

    def fire_bullet(self):
        pass

    def update(self):
        for game_object in game_world.get_objects(2):
            if math.sqrt((game_object.x - self.x)**2 + (game_object.y - self.y)**2 ) < 20:
                print('fuck')



    def draw(self):
        self.image.clip_composite_draw(0, 800, 200, 200, 0, '', self.x, self.y, 100, 100)