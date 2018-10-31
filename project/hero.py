from pico2d import *
import math
import random

import game_world

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


# Boy States

class IdleState:

    @staticmethod
    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.hor_speed += 1
        if event == LEFT_DOWN:
            hero.hor_speed -= 1
        if event == UP_DOWN:
            hero.ver_speed +=1
        if event == DOWN_DOWN:
            hero.ver_speed -= 1

        if event == RIGHT_UP:
            hero.hor_speed -= 1
        if event == LEFT_UP:
            hero.hor_speed += 1
        if event == UP_UP:
            hero.ver_speed -= 1
        if event == DOWN_UP:
            hero.ver_speed += 1


    @staticmethod
    def exit(hero, event):
        # fill here
        pass

    @staticmethod
    def do(hero):
        pass
        # fill here

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(0, 0, 100, 100, hero.x, hero.y)



class RunState:

    @staticmethod
    def enter(hero, event):
        if event == RIGHT_DOWN:
            hero.hor_speed += 1
        if event == LEFT_DOWN:
            hero.hor_speed -= 1
        if event == UP_DOWN:
            hero.ver_speed += 1
        if event == DOWN_DOWN:
            hero.ver_speed -= 1

        if event == RIGHT_UP:
            hero.hor_speed -= 1
        if event == LEFT_UP:
            hero.hor_speed += 1
        if event == UP_UP:
            hero.ver_speed -= 1
        if event == DOWN_UP:
            hero.ver_speed += 1


    @staticmethod
    def exit(hero, event):
        # fill here
        pass

    @staticmethod
    def do(hero):
        hero.x += hero.hor_speed
        hero.y += hero.ver_speed

    @staticmethod
    def draw(hero):
        hero.image.clip_draw(0,0,100,100,hero.x,hero.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP:IdleState, DOWN_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState}
}

class Hero:

    def __init__(self):
        self.x, self.y = 1600 / 2, 900/2
        self.image = load_image('character-sprite-.png')
        self.hor_speed = 0
        self.ver_speed = 0
        self.dir_x = 0
        self.dir_y = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire(self):
        # fill here
        pass



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


