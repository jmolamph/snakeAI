# james molamphy jmolamph

import random


class Food:
    def __init__(self, width, height, block):
        self._X = None
        self._Y = None
        self._width = width
        self._height = height
        self._block = block

        self.spawn()

    def spawn(self):
        """
        updates the X and Y coordinates to a random position on the board
        """
        self._X = round(random.randrange(0, self._width - self._block) / float(self._block)) * float(self._block)
        self._Y = round(random.randrange(0, self._height - self._block) / float(self._block)) * float(self._block)

    def get_x(self):
        return self._X

    def get_y(self):
        return self._Y