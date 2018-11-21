from pico2d import *
import math
import game_world
import game_framework

# Bullet Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
GUN_SPEED_KMPH = 10.0  # Km / Hour
GUN_SPEED_MPM = (GUN_SPEED_KMPH * 1000.0 / 60.0)
GUN_SPEED_MPS = (GUN_SPEED_MPM / 60.0)
GUN_SPEED_PPS = (GUN_SPEED_MPS * PIXEL_PER_METER)

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
        if state == 0:
            self.damage = 5
            self.bullet_speed = GUN_SPEED_PPS
        if state == 1 or state == 2:
            self.damage = 5
            self.bullet_speed = GUN_SPEED_PPS*2
        elif state == 3:
            self.damage = 50
            self.bullet_speed = GUN_SPEED_PPS*2

    def draw(self):
        if self.state == 0:
            self.image.clip_composite_draw(980 - 20, 980 - 50, 40, 40, self.dir, '', self.x, self.y, 40, 40)
        if self.state == 1 or self.state == 2:
            self.image.clip_composite_draw(980-20, 980-20, 40, 40, self.dir, '', self.x, self.y, 40, 40)
        elif self.state == 3:
            self.image.clip_composite_draw(900-50, 965-50, 100, 100, self.dir, '', self.x, self.y, 40, 40)

    def update(self):
        self.x += self.velocity_x*self.bullet_speed * game_framework.frame_time
        self.y += self.velocity_y*self.bullet_speed * game_framework.frame_time

        if self.x < 0 or self.x > 1280 or self.y < 0 or self.y > 1024:
            game_world.remove_object(self)

        if self.state == 0:
            pass


