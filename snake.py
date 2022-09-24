# james molamphy jmolamph

import random


class Snake:
    def __init__(self, width, height, block):
        self._width = width
        self._height = height
        self._block = block
        self._speed = 20
        self._X1 = None
        self._Y1 = None
        self._length = 1
        self._list = []

        self.spawn()

    def spawn(self):
        """
        updates the X and Y coordinates to a random position on the board
        """
        self._X1 = round(random.randrange(0, self._width - self._block) / float(self._block)) * float(self._block)
        self._Y1 = round(random.randrange(0, self._height - self._block) / float(self._block)) * float(self._block)

    def set_position(self, x, y):
        """
        updates the X and Y coordinates of the snake
        """
        self._X1 += x
        self._Y1 += y

    def set_length(self):
        self._length += 1
        self._speed += 1

    def get_x(self):
        return self._X1

    def get_y(self):
        return self._Y1

    def get_length(self):
        return self._length

    def get_list(self):
        return self._list

    def get_speed(self):
        return self._speed

    def append_list(self, block):
        self._list.append(block)

    def delete_tail(self):
        del self._list[0]
