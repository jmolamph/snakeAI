import random


class Food:
    def __init__(self, width, height, block):
        self._X = None
        self._Y = None
        self.width = width
        self.height = height
        self.block = block

        self.spawn()

    def spawn(self):
        self._X = round(random.randrange(0, self.width - self.block) / 10.0) * 10.0
        self._Y = round(random.randrange(0, self.height - self.block) / 10.0) * 10.0

    def get_x(self):
        return self._X

    def get_y(self):
        return self._Y