from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('map_purple.png')
        self.image2 = load_image('post_box.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(500, 400)
        self.image.draw(1200, 400)
        self.image2.draw(600, 130)
