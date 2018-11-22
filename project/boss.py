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



class Boss:
    def __init__(self):
        self.body_HP = 100
        self.body_x , self.body_y  = 1280//2 , 800
        self.body_image = load_image('boss-sprite.png')
        self.dir_body_to_hero = 0
        self.body_state = 0

        self.left_arm_HP = 100
        self.left_arm_x, self.left_arm_y = self.body_x - 60, self.body_y - 40
        self.left_arm_image = load_image('boss-arm.png')
        self.left_arm_state = 0

        self.right_arm_HP = 100
        self.right_arm_x, self.right_arm_y = self.body_x + 60, self.body_y - 40
        self.right_arm_image = load_image('boss-arm.png')
        self.right_arm_state = 0



    def fire_bullet(self):
        bullet = Bullet(self.body_x, self.body_y, hero.find_x() + random.randint(-20, 20), hero.find_y() + random.randint(-20, 20),
                        0, self.dir_body_to_hero)
        game_world.add_object(bullet, 3)

    def update(self):
        Boss.body_update(self)
        Boss.right_arm_update(self)
        Boss.left_arm_update(self)

    def right_arm_update(self):
        if self.right_arm_state == 0:
            pass

    def left_arm_update(self):
        pass


    def body_update(self):
        for hero_bullet in game_world.get_objects(2):
            if ((hero_bullet.x - self.body_x)**2 + (hero_bullet.y - (self.body_y + 50))**2 ) < (PIXEL_PER_METER*2)**2 or \
                    ((hero_bullet.x - self.body_x)**2 + (hero_bullet.y - (self.body_y - 100))**2 ) < (PIXEL_PER_METER*2)**2 or \
                ((hero_bullet.x - self.body_x) ** 2 + (hero_bullet.y - (self.body_y)) ** 2) < (PIXEL_PER_METER * 2) ** 2:
                #라이플은 단순한 데미지
                if hero_bullet.state == 1:
                    self.body_HP -= hero_bullet.damage
                #샷건은 데미지와 넉백
                elif hero_bullet.state == 2:
                    self.body_HP -= hero_bullet.damage
                #바주카는 스플래시 데미지
                elif hero_bullet.state == 3:
                    self.body_HP -= hero_bullet.damage
                    explosion = Explosion(hero_bullet.x, hero_bullet.y)
                    game_world.add_object(explosion, 4)
                game_world.remove_object(hero_bullet)

    def draw(self):
        self.body_image.clip_composite_draw(280, 540-150, 280, 150, 0, '', self.body_x, self.body_y, 280*2.0, 150*2.0)
        self.draw_left_arm()
        self.draw_right_arm()



    def draw_right_arm(self):
        if self.right_arm_state == 0:
            self.right_arm_image.clip_composite_draw(0, 535 - 50, 70, 50, 0, '', self.right_arm_x, self.right_arm_y,
                                                 70 * 2.0, 50 * 2.0)

    def draw_left_arm(self):
        if self.left_arm_state == 0:
            self.left_arm_image.clip_composite_draw(0, 535 - 50, 70, 50, 0, 'h', self.left_arm_x, self.left_arm_y,
                                                70 * 2.0, 50 * 2.0)



