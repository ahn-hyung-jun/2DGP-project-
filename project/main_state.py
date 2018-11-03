import random
import json
import os
import game_world

from pico2d import *

import game_framework
from map import Map
from hero import Hero

import hero

name = "MainState"

maps = None


def enter():
    global maps
    global hero
    hero = Hero()
    maps = [[Map(i,j) for i in range(100)] for j in range(100)]
    game_world.add_object(hero, 1)

def exit():
    game_world.clear()



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


def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()

    for i in range(100):
        for j in range(100):
            maps[j][i].draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





