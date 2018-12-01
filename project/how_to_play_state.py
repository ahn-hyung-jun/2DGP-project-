import game_framework
from pico2d import *
import title_state
import fail_state
import main_state
name = "HowToPlayState"
image = None


def enter():
    global image1
    global image2
    global state
    state = 1
    image1 = load_image('how_to_play1.PNG')
    image2 = load_image('how_to_play2.png')
    global font
    font = load_font('ENCR10B.TTF', 16)

def exit():
    global image1
    del(image1)
    global image2
    del(image2)


def update():
    pass


def draw():
    clear_canvas()
    if state == 1:
        image1.draw(1280//2,1024//2)
    elif state == 2:
        image2.draw(1280//2,1024//2)
    font.draw(1280/2, 300, 'Press Space Key to Start', (0, 0, 0))
    update_canvas()

def handle_events():
    global state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if state == 1:
                    state += 1
                elif state == 2:
                    game_framework.change_state(main_state)

def pause():
    pass


def resume():
    pass






