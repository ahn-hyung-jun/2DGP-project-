import game_framework
from pico2d import *
import main_state

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')
    global font
    font = load_font('ENCR10B.TTF', 16)

def exit():
    global image
    del(image)


def update():
    pass


def draw():
    clear_canvas()
    image.draw(1280/2,1024/2)
    font.draw(1280/2, 300, 'Press Space Key to Start', (0, 0, 0))
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
    pass

def pause():
    pass


def resume():
    pass






