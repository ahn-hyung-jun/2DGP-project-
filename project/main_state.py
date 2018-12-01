import random
import json
import os
import game_world

from pico2d import *

import game_framework
from map import Map
from hero import Hero
from boss import Boss
from boss import Boss_right_arm
from boss import Boss_left_arm
from cursor import Cursor
from enemy_genarate import Enemy_genarate

import hero

name = "MainState"
maps = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global boss_gauge
    boss_gauge = 0
    global hero
    global cursor
    global boss
    global boss_right_arm
    global boss_left_arm
    global enemy_genarate

    map = Map()
    cursor = Cursor()
    boss = Boss()
    boss_right_arm = Boss_right_arm()
    boss_left_arm = Boss_left_arm()
    hero = Hero()

    hide_cursor()
    game_world.add_object(map,0)

    enemy_genarate = Enemy_genarate()
    game_world.add_object(hero, 1)
    game_world.add_object(cursor, 4)

    game_world.add_object(enemy_genarate, 0)

def exit():
    game_world.clear()

def get_right_arm_state():
    return boss_right_arm.state

def get_left_arm_state():
    return boss_left_arm.state

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            hero.handle_event(event)
            cursor.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    global boss_gauge
    if boss_gauge == 60:
        game_world.add_object(boss, 1)
        game_world.add_object(boss_right_arm,1)
        game_world.add_object(boss_left_arm,1)
        boss_gauge+=1

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





