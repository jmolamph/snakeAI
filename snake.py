import random


class Snake:
    def __init__(self):
        self._X1 = 300
        self._Y1 = 300
        self._length = 1

    def update_position(self, x, y):
        self._X1 += x
        self._Y1 += y

    def update_length(self):
        self._length += 1

    def get_x(self):
        return self._X1

    def get_y(self):
        return self._Y1

    def get_length(self):
        return self._length
