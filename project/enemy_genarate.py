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
        self.fuck = 0

    def update(self):
        if self.enemy_num > 0:
            self.enemy_num -= 1
            self.generate()

    def draw(self):
        pass

    def generate(self):
        enemy = Enemy(random.randint(0, 1280), random.randint(0, 1024))
        game_world.add_object(enemy, 1)






