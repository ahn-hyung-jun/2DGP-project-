import random
import json
import os
import game_world
import main_state
from pico2d import *
import hero
from boss_bullet import Boss_bullet
import random
import game_framework
import enemy

from enemy import Enemy

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def pattern_5(fire, x, y, state):
    #dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%2 == 0:
        bullet = Boss_bullet(x, y, math.radians(random.randint(0,360)), state)
        game_world.add_object(bullet, 3)

def pattern_6(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%8 == 0:
        bullet = Boss_bullet(x, y, dir, state)
        game_world.add_object(bullet, 3)

def pattern_2():
    pass
