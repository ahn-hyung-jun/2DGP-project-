from pico2d import *
import math
import random


import game_world
import hero
import enemy_genarate
import main_state
from bullet import Bullet
from explosion import Explosion
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

# Enemy Run Speed
PIXEL_PER_METER =  (10.0/0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)



# Hero Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Boss_body:
    def __init__(self):
        self.HP = 100
        self.x , self.y  = 1280//2 , 800
        self.fire_timer = 1000
        self.fire_speed = 10
        self.image = load_image('boss-sprite.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir_to_hero = 0
        self.dir_to_move = 0
        self.speed = RUN_SPEED_PPS
        self.timer = 3

    def fire_bullet(self):
        bullet = Bullet(self.x, self.y, hero.find_x() + random.randint(-20, 20), hero.find_y() + random.randint(-20, 20),
                        0, self.dir_to_hero)
        game_world.add_object(bullet, 3)


    def update(self):
        for hero_bullet in game_world.get_objects(2):
            if ((hero_bullet.x - self.x)**2 + (hero_bullet.y - (self.y + 50))**2 ) < (PIXEL_PER_METER*2)**2 or \
                    ((hero_bullet.x - self.x)**2 + (hero_bullet.y - (self.y - 200))**2 ) < (PIXEL_PER_METER*4)**2:
                #라이플은 단순한 데미지
                if hero_bullet.state == 1:
                    self.HP -= hero_bullet.damage
                #샷건은 데미지와 넉백
                elif hero_bullet.state == 2:
                    self.HP -= hero_bullet.damage
                #바주카는 스플래시 데미지
                elif hero_bullet.state == 3:
                    self.HP -= hero_bullet.damage
                    explosion = Explosion(self.x, self.y)
                    game_world.add_object(explosion, 0)
                game_world.remove_object(hero_bullet)

    def draw(self):
        self.image.clip_composite_draw(280, 540-150, 280, 150, 0, '', self.x, self.y, 280*2.0, 150*2.0)
