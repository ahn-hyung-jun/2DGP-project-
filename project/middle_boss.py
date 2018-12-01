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



class Middle_boss:
    def __init__(self):
        self.body_x, self.body_y = 1280 // 2, 800

        self.HP = 700
        self.x, self.y = self.body_x + 60, self.body_y - 80
        # self.right_arm_x, self.right_arm_y = 600,500
        self.right_arm_image = load_image('boss-arm.png')
        self.state = 2
        self.fire_time = 1
        self.degree = 0
        self.fire_speed = 1
        self.dir_to_move = 0
        self.dir_to_hero = 0
        self. timer = 3
        self.build_behavior_tree()


    def fire_bullet(self):
        if self.state == 4:
            bullet = Bullet(self.x, self.y, hero.find_x() + random.randint(-20, 20), hero.find_y() + random.randint(-20, 20),
                        0, self.dir_to_hero)
        if self.state == 5:
            bullet = Bullet(self.x, self.y, hero.find_x() + random.randint(-20, 20),
                            hero.find_y() + random.randint(-20, 20),
                            -1, self.dir_to_hero)
        game_world.add_object(bullet, 3)

    def move_to_hero(self):
        self.dir_to_move = math.atan2(hero.find_y() - self.y, hero.find_x() - self.x)
        return BehaviorTree.SUCCESS

    def find_hero(self):
        hero_x = hero.find_x()
        hero_y = hero.find_y()
        distance = (hero_x - self.x) ** 2 + (hero_y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 20) ** 2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def shot_to_hero(self):
        self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.timer += 1.0
            self.dir_to_move = random.random() * 2 * math.pi

        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS

    def update(self):
        self.bt.run()
        self.body_x += self.speed * math.cos(self.dir_to_move) * game_framework.frame_time
        self.body_y += self.speed * math.sin(self.dir_to_move) * game_framework.frame_time
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
            self.state = random.randint(2,6)
        elif self.HP < 0:
            main_state.boss_gauge += 10
            main_state.middle_boss_exist = -1
            game_world.remove_object(self)


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

    def build_behavior_tree(self):
        find_hero_node = LeafNode("Find Hero", self.find_hero)
        shot_to_hero_node = LeafNode("Shot to Hero", self.shot_to_hero)
        move_to_hero_node = LeafNode("Move to hero", self.move_to_hero)
        shot_node = SequenceNode("Move")
        shot_node.add_children(find_hero_node, shot_to_hero_node)
        shot_move_node = SelectorNode("ShotMove")
        shot_move_node.add_children(shot_node, move_to_hero_node)
        self.bt = BehaviorTree(shot_move_node)

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
