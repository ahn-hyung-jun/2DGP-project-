from pico2d import *
import math
import random

from bullet import Bullet
import game_world
import hero
import enemy_genarate
import bullet



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
    def __init__(self , x = 400 , y = 300):
        self.hp = 100
        self.x , self.y  = x,y
        self.fire_timer = 1000
        self.fire_speed = 10
        self.image = load_image('hero_sprite.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 0

    def fire_bullet(self):
        pass

    def update(self):
        for game_object in game_world.get_objects(2):
            if math.sqrt((game_object.x - self.x)**2 + (game_object.y - self.y)**2 ) < 20:
                self.hp -= game_object.damage
                game_world.remove_object(game_object)
        self.dir = math.atan2(hero.find_y() - self.y, hero.find_x() - self.x) - math.pi / 2


        self.fire_timer -= self.fire_speed
        if self.fire_timer < 0:
            pass

        if self.hp <= 0:
            game_world.remove_enemy(self)
            enemy_genarate.Enemy_genarate.generate(self)



    def draw(self):
        self.image.clip_composite_draw(0, 800, 200, 200, self.dir, '', self.x, self.y, 100, 100)
        self.font.draw(self.x - 60, self.y + 50, '(B %3.2i / 100)' % self.hp, (255, 255, 0))