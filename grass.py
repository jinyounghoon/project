from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('map_purple.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)
        self.image.draw(1200, 400)
