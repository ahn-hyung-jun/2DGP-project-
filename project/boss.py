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
import boss_pattern
import victory_state
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

# Enemy Run Speed
PIXEL_PER_METER =  (10.0/0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)



# Hero Action Speed
TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 60

def get_distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2



class Boss_right_arm:
    def __init__(self):
        self.body_x, self.body_y = 1280 // 2, 800

        self.HP = 2000
        self.x, self.y = self.body_x + 60, self.body_y - 80
        # self.right_arm_x, self.right_arm_y = 600,500
        self.right_arm_image = load_image('boss-arm.png')
        self.state = -1
        self.fire_time = 1
        self.degree = 0
        self.fire_speed = 1


    def update(self):
        global right_arm_state
        right_arm_state = self.state
        self.fire_speed += game_framework.frame_time*FRAMES_PER_ACTION
        if self.fire_speed > 1:
            self.fire_speed = 0
            self.fire_time+=1
            self.degree += 1
        #self.fire_time = self.fire_time + self.fire_speed * game_framework.frame_time*FRAMES_PER_ACTION
        #self.degree = self.degree + 1 * game_framework.frame_time * FRAMES_PER_ACTION
        if int(self.fire_time)%300 == 0 and self.HP > 0:
            self.state = random.randint(1,6)
        elif self.HP < 0:
            self.state=0


        if self.state == 0:
            self.x, self.y = self.body_x + 60, self.body_y - 80
            boss_pattern.pattern_0(self.fire_time,self.x, self.y, 1)


        if self.state == 1:
            self.x, self.y = self.body_x + 120, self.body_y - 80
            boss_pattern.pattern_1(self.fire_time, self.x + 40, self.y - 10, 1)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 60) < (
                        PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 2:
            self.x, self.y = self.body_x + 120, self.body_y - 80
            boss_pattern.pattern_2(self.fire_time, self.x + 45, self.y + 5, 1)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 60) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 3:
            self.x, self.y = self.body_x + 120, self.body_y - 80
            boss_pattern.pattern_3(self.fire_time, self.x + 20, self.y - 60, 1)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y) < (PIXEL_PER_METER ) ** 2 \
                    or get_distance(hero_bullet.x, hero_bullet.y, self.x - 30, self.y+30)< (PIXEL_PER_METER) ** 2 \
                    or get_distance(hero_bullet.x, hero_bullet.y, self.x + 30, self.y-30)< (PIXEL_PER_METER) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 4:
            self.x, self.y = self.body_x + 90, self.body_y - 80
            boss_pattern.pattern_4(self.fire_time, self.x + 0, self.y - 10, 1, self.degree)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 5:
            self.x, self.y = self.body_x + 70, self.body_y - 80
            boss_pattern.pattern_5(self.fire_time, self.x + 10, self.y - 70, 1)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2\
                        or get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y - 40) < (PIXEL_PER_METER) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 6:
            self.x, self.y = self.body_x + 70, self.body_y - 80
            boss_pattern.pattern_6(self.fire_time, self.x+20, self.y-15, 1)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

    def draw(self):
        if self.state == 0 or self.state == -1:
            self.right_arm_image.clip_composite_draw(0, 535 - 95, 70, 95, 0, '', self.x, self.y,
                                                     70 * 2.0, 95 * 2.0)

        elif self.state == 1:
            self.right_arm_image.clip_composite_draw(70, 535 - 95, 80, 95, 0, '', self.x, self.y,
                                                     80 * 2.0, 95 * 2.0)

        elif self.state == 2:
            self.right_arm_image.clip_composite_draw(150, 535 - 95, 80, 95, 0, '', self.x, self.y,
                                                     80 * 2.0, 95 * 2.0)

        elif self.state == 3:
            self.right_arm_image.clip_composite_draw(230, 535 - 95, 60, 95, 0, '', self.x, self.y,
                                                     60 * 2.0, 95 * 2.0)

        elif self.state == 4:
            self.right_arm_image.clip_composite_draw(290, 535 - 95, 40, 95, 0, '', self.x, self.y,
                                                     40 * 2.0, 95 * 2.0)

        elif self.state == 5:
            self.right_arm_image.clip_composite_draw(330, 535 - 95, 40, 95, 0, '', self.x, self.y,
                                                     40 * 2.0, 95 * 2.0)
        elif self.state == 6:
            self.right_arm_image.clip_composite_draw(370, 535 - 95, 50, 95, 0, '', self.x, self.y,
                                                     50 * 2.0, 95 * 2.0)

class Boss_left_arm:
    def __init__(self):
        self.body_x, self.body_y = 1280 // 2, 800

        self.HP = 2000
        self.x, self.y = self.body_x - 60, self.body_y - 80
        self.left_arm_image = load_image('boss-arm.png')
        self.state = -1

        self.fire_time = 1
        self.degree = 0
        self.fire_speed = 1

        self.degree =1

    def update(self):
        global left_arm_state
        left_arm_state = self.state
        self.fire_speed += game_framework.frame_time * FRAMES_PER_ACTION
        if self.fire_speed > 1:
            self.fire_speed = 0
            self.fire_time += 1
            self.degree += 1
        #self.fire_time = self.fire_time + self.fire_speed* game_framework.frame_time*FRAMES_PER_ACTION
        if int(self.fire_time) % 300 == 0 and self.HP > 0:
            self.state = random.randint(1, 6)
        elif self.HP < 0:
            self.state = 0
        #self.degree = self.degree + 1* game_framework.frame_time*FRAMES_PER_ACTION
        if self.state == 0:
            self.x, self.y = self.body_x - 60, self.body_y - 80
            boss_pattern.pattern_0(self.fire_time, self.x, self.y, 1)

        if self.state == 1:
            self.x, self.y = self.body_x - 120, self.body_y - 80
            boss_pattern.pattern_1(self.fire_time, self.x - 40, self.y - 10, 0)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 60) < (
                        PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 2:
            self.x, self.y = self.body_x - 120, self.body_y - 80
            boss_pattern.pattern_2(self.fire_time, self.x - 45, self.y + 5, 0)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 60) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 3:
            self.x, self.y = self.body_x - 120, self.body_y - 80
            boss_pattern.pattern_3(self.fire_time, self.x - 20, self.y - 60, 0)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y) < (PIXEL_PER_METER ) ** 2 \
                    or get_distance(hero_bullet.x, hero_bullet.y, self.x - 30, self.y+30)< (PIXEL_PER_METER) ** 2 \
                    or get_distance(hero_bullet.x, hero_bullet.y, self.x + 30, self.y-30)< (PIXEL_PER_METER) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 4:
            self.x, self.y = self.body_x - 90, self.body_y - 80
            boss_pattern.pattern_4(self.fire_time, self.x + 0, self.y - 10, 0, self.degree)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 5:
            self.x, self.y = self.body_x - 70, self.body_y - 80
            boss_pattern.pattern_5(self.fire_time, self.x + 10, self.y - 70, 0)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2\
                        or get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y - 40) < (PIXEL_PER_METER) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

        if self.state == 6:
            self.x, self.y = self.body_x - 70, self.body_y - 80
            boss_pattern.pattern_6(self.fire_time, self.x + 20, self.y - 15, 0)
            for hero_bullet in game_world.get_objects(2):
                if get_distance(hero_bullet.x, hero_bullet.y, self.x, self.y + 40) < (PIXEL_PER_METER * 2) ** 2:
                    # 라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    # 바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

    def draw(self):
        if self.state == 0 or self.state == -1:
            self.left_arm_image.clip_composite_draw(0, 535 - 95, 70, 95, 0, 'h', self.x, self.y,
                                                    70 * 2.0, 95 * 2.0)

        elif self.state == 1:
            self.left_arm_image.clip_composite_draw(70, 535 - 95, 80, 95, 0, 'h', self.x, self.y,
                                                    80 * 2.0, 95 * 2.0)

        elif self.state == 2:
            self.left_arm_image.clip_composite_draw(150, 535 - 95, 80, 95, 0, 'h', self.x, self.y,
                                                    80 * 2.0, 95 * 2.0)

        elif self.state == 3:
            self.left_arm_image.clip_composite_draw(230, 535 - 95, 60, 95, 0, 'h', self.x, self.y,
                                                    60 * 2.0, 95 * 2.0)

        elif self.state == 4:
            self.left_arm_image.clip_composite_draw(290, 535 - 95, 40, 95, 0, 'h', self.x, self.y,
                                                     40 * 2.0, 95 * 2.0)

        elif self.state == 5:
            self.left_arm_image.clip_composite_draw(330, 535 - 95, 40, 95, 0, 'h', self.x, self.y,
                                                    40 * 2.0, 95 * 2.0)

        elif self.state == 6:
            self.left_arm_image.clip_composite_draw(370, 535 - 95, 50, 95, 0, 'h', self.x, self.y,
                                                    50 * 2.0, 95 * 2.0)

class Boss:
    def __init__(self):
        self.HP = 4000
        self.x , self.y  = 1280//2 , 800
        self.body_image = load_image('boss-sprite.png')
        self.dir_body_to_hero = 0
        self.body_state = 0

        self.frame = 0

        self.state = 0

        self.fire_time = 0
        self.degree = 0
        self.fire_speed = 1

        self.degree = 0


    def update(self):
        #self.fire_time = self.fire_time + self.fire_speed* game_framework.frame_time*FRAMES_PER_ACTION
        self.fire_speed += game_framework.frame_time * FRAMES_PER_ACTION
        if self.fire_speed > 1:
            self.fire_speed = 0
            self.fire_time += 1
            self.degree += 1
        if int(self.fire_time) % 300 == 0 and self.HP > 0 and self.state != 0:
            self.state = random.randint(1, 3)
            pass
        elif self.HP < 0:
            game_framework.change_state(victory_state)
        #self.degree = self.degree + 1* game_framework.frame_time*FRAMES_PER_ACTION
        Boss.body_update(self)

        if main_state.get_left_arm_state() == 0 and main_state.get_right_arm_state() == 0 and self.state == 0:
            self.state = random.randint(1,3)




    def body_update(self):
        if self.state == 1:
            boss_pattern.pattern_head_1(self.fire_time, self.x, self.y, 2)

        elif self.state == 2:
            boss_pattern.pattern_head_2(self.fire_time,self.x,self.y,2, self.degree)

        elif self.state == 3:
            boss_pattern.pattern_head_3(self.fire_time,self.x, self.y, 6, self.degree)


        if self.state != -1:
            if self.HP < 2000:
                boss_pattern.pattern_tentacle(self.fire_time, self.x + 250, self.y + 50, 0)
                boss_pattern.pattern_tentacle(self.fire_time, self.x + 250, self.y - 50, 0)
                boss_pattern.pattern_tentacle(self.fire_time, self.x - 250, self.y + 50, 0)
                boss_pattern.pattern_tentacle(self.fire_time, self.x - 250, self.y - 50, 0)
            for hero_bullet in game_world.get_objects(2):
                if ((hero_bullet.x - self.x)**2 + (hero_bullet.y - (self.y + 50))**2 ) < (PIXEL_PER_METER*2)**2 or \
                        ((hero_bullet.x - self.x)**2 + (hero_bullet.y - (self.y - 100))**2 ) < (PIXEL_PER_METER*2)**2 or \
                    ((hero_bullet.x - self.x) ** 2 + (hero_bullet.y - (self.y)) ** 2) < (PIXEL_PER_METER * 2) ** 2:
                    #라이플은 단순한 데미지
                    if hero_bullet.state == 1 or hero_bullet.state == 2:
                        self.HP -= hero_bullet.damage
                    #바주카는 스플래시 데미지
                    elif hero_bullet.state == 3:
                        self.HP -= hero_bullet.damage
                        explosion = Explosion(hero_bullet.x, hero_bullet.y)
                        game_world.add_object(explosion, 4)
                    game_world.remove_object(hero_bullet)

    def draw(self):
        self.body_image.clip_composite_draw(280, 540-150, 280, 150, 0, '', self.x, self.y, 280*2.0, 150*2.0)











