import random
import json
import os
import game_world
import main_state
from pico2d import *
import hero
from boss_bullet import Boss_bullet
import random
import enemy_genarate
import game_framework
import enemy

from enemy import Enemy

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def pattern_0(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%50 == 0:
        bullet = Boss_bullet(x, y, dir, state)
        game_world.add_object(bullet, 3)

def pattern_1(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%50 == 0:
        enemy = Enemy(x, y, random.randint(4,5))
        game_world.add_object(enemy, 1)


def pattern_2(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%40 == 0:
        bullet = Boss_bullet(x, y, dir, state+3)
        game_world.add_object(bullet, 3)

def pattern_3(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%8 == 0:
        bullet1 = Boss_bullet(x, y, dir - math.pi / 10 , state)
        game_world.add_object(bullet1, 3)

    elif int(fire)%8 == 1:
        bullet2 = Boss_bullet(x, y, dir + math.pi / 10, state)
        game_world.add_object(bullet2, 3)


def pattern_4(fire, x, y, state, degree):
    #dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%4 == 0:
        bullet1 = Boss_bullet(x, y, math.radians(degree), state)
        game_world.add_object(bullet1, 3)
    elif int(fire)%4 == 1:
        bullet2 = Boss_bullet(x, y, math.radians(degree) - math.pi / 2, state)
        game_world.add_object(bullet2, 3)
    elif int(fire)%4 == 2:
        bullet3 = Boss_bullet(x, y, math.radians(degree) - math.pi, state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%4 == 3:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi / 2, state)
        game_world.add_object(bullet4, 3)


def pattern_5(fire, x, y, state):
    #dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%1 == 0:
        bullet = Boss_bullet(x, y, math.radians(random.randint(0,360)), state)
        game_world.add_object(bullet, 3)

def pattern_6(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%6 == 0:
        bullet = Boss_bullet(x, y, dir, state)
        game_world.add_object(bullet, 3)

def pattern_tentacle(fire,x,y,state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%13 == 0:
        bullet = Boss_bullet(x, y, dir + math.radians(random.randint(-5,5)), state)
        game_world.add_object(bullet, 3)

def pattern_head_1(fire, x, y, state):
    dir = math.atan2(hero.find_y() - y, hero.find_x() - x)
    if int(fire)%100 == 0:
        bullet = Boss_bullet(x, y, dir, state+3)
        game_world.add_object(bullet, 3)

def pattern_head_2(fire, x, y, state, degree):
    if int(fire)%8 == 0:
        bullet1 = Boss_bullet(x, y, math.radians(degree), state)
        game_world.add_object(bullet1, 3)
    elif int(fire)%8 == 1:
        bullet2 = Boss_bullet(x, y, math.radians(degree) - math.pi / 4, state)
        game_world.add_object(bullet2, 3)
    elif int(fire)%8 == 2:
        bullet3 = Boss_bullet(x, y, math.radians(degree) - math.pi / 4 * 2, state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 3:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi / 4 * 3, state)
        game_world.add_object(bullet4, 3)
    elif int(fire)%8 == 4:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi / 4, state)
        game_world.add_object(bullet4, 3)
    elif int(fire)%8 == 5:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi / 4*2, state)
        game_world.add_object(bullet4, 3)
    elif int(fire)%8 == 6:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi / 4*3, state)
        game_world.add_object(bullet4, 3)
    elif int(fire)%8 == 7:
        bullet4 = Boss_bullet(x, y, math.radians(degree) + math.pi, state)
        game_world.add_object(bullet4, 3)

def pattern_head_3(fire, x, y, state, degree):
    if int(fire)%8 == 0:
        bullet1 = Boss_bullet(x, y, math.radians(degree+45), state)
        game_world.add_object(bullet1, 3)
    elif int(fire)%8 == 1:
        bullet2 = Boss_bullet(x, y, math.radians(degree+90), state)
        game_world.add_object(bullet2, 3)
    elif int(fire)%8 == 2:
        bullet3 = Boss_bullet(x, y, math.radians(degree+135), state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 3:
        bullet3 = Boss_bullet(x, y, math.radians(degree+180), state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 4:
        bullet3 = Boss_bullet(x, y, math.radians(degree+225), state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 5:
        bullet3 = Boss_bullet(x, y, math.radians(degree+270), state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 6:
        bullet3 = Boss_bullet(x, y, math.radians(degree+315), state)
        game_world.add_object(bullet3, 3)
    elif int(fire)%8 == 7:
        bullet3 = Boss_bullet(x, y, math.radians(degree+360), state)
        game_world.add_object(bullet3, 3)

