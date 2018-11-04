import random
import json
import os
import game_world

from pico2d import *

import game_framework
import enemy
from enemy import Enemy


class Enemy_genarate:
    def __init__(self):
        self.enemy_num = 20

    def update(self):
        if self.enemy_num > 0:
            self.enemy_num -= 1
            self.generate()

    def draw(self):
        pass

    def generate(self):
        enemy = Enemy(random.randint(0,800), random.randint(0,600))
        game_world.add_object(enemy, 1)




