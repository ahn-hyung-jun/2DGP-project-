from pico2d import *
import math
import game_world


# Bullet Speed
PIXEL_PER_METER =  (1.0/0.3)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity_x = 1, velocity_y = 1, state = 1, dir = 0):
        if Bullet.image == None:
            self.image = load_image('hero_sprite.png')
        self.velocity_x = (velocity_x - x) / math.sqrt((velocity_x - x)**2 +(velocity_y-y)**2)
        self.velocity_y = (velocity_y - y) / math.sqrt((velocity_x - x)**2 +(velocity_y-y)**2)
        self.x, self.y = x + self.velocity_x*30, y + self.velocity_y*30
        self.state = state
        self.dir = dir
        if state == 1 or state == 2:
            self.damage = 5
        elif state == 3:
            self.damage = 50

    def draw(self):
        if self.state == 1 or self.state == 2:
            self.image.clip_composite_draw(980-20, 980-20, 40, 40, self.dir, '', self.x, self.y, 40, 40)
        elif self.state == 3:
            self.image.clip_composite_draw(900-50, 965-50, 100, 100, self.dir, '', self.x, self.y, 40, 40)

    def update(self):
        self.x += self.velocity_x*5
        self.y += self.velocity_y*5

        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 600:
            game_world.remove_object(self)
