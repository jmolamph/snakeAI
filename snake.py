import random


class Snake:
    def __init__(self, width, height, block):
        self._width = width
        self._height = height
        self._block = block
        self._X1 = round(random.randrange(0, self._width - self._block) / 10.0) * 10.0
        self._Y1 = round(random.randrange(0, self._height - self._block) / 10.0) * 10.0
        self._length = 1
        self._list = []

    def set_position(self, x, y):
        """
        updates the x and y coordinates of the
        """
        self._X1 += x
        self._Y1 += y

    def set_length(self):
        self._length += 1

    def get_x(self):
        return self._X1

    def get_y(self):
        return self._Y1

    def get_length(self):
        return self._length

    def get_list(self):
        return self._list

    def append_list(self, block):
        self._list.append(block)

    def delete_tail(self):
        del self._list[0]
