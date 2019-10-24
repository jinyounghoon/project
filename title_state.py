import game_framework
from pico2d import *

import main_state

WIDTH, HEIGHT = 800, 600

name = "TitleState"
image = None
image2 = None


def enter():
    global image, image2
    image = load_image('title.png')
    image2 = load_image('title2.png')

def exit():
    global image, image2
    del(image)
    del(image2)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image2.draw(WIDTH//2, HEIGHT//2, 800, 600)
    image.draw(400, 500, 270, 150)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






