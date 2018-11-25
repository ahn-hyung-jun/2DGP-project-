import random
import json
import os
import game_world
import main_state
from pico2d import *

import game_framework
import enemy

from enemy import Enemy


class Enemy_genarate:
    def __init__(self):
        self.enemy_num = 20
        self.boss_gauge = 0
        self.boss_exist = False

    def update(self):
        if self.enemy_num > 0:
            self.enemy_num -= 1
            self.generate()


    def draw(self):
        pass

    def generate(self):
        random_pos = random.randint(0,3)
        random_state = random.randint(4,5)

        if random_pos == 0:
            enemy = Enemy(random.randint(0, 1280), random.randint(1024, 1124), random_state)
            game_world.add_object(enemy, 1)
        elif random_pos == 1:
            enemy = Enemy(random.randint(1280, 1380), random.randint(0, 1024), random_state)
            game_world.add_object(enemy, 1)
        elif random_pos == 2:
            enemy = Enemy(random.randint(0, 1280), random.randint(-100, 100), random_state)
            game_world.add_object(enemy, 1)
        elif random_pos == 3:
            enemy = Enemy(random.randint(-100, 0), random.randint(0, 1024), random_state)
            game_world.add_object(enemy, 1)
