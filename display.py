# -*- coding: utf-8 -*-

class Window(object):
    def __init__(self, start_x, start_y, height, width):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width

    def load_buffer(self, buff):
        pass

class Quadrant(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[0 for _ in range(w)] for _ in range(h)]

    def append_row(self):
        self.h += 1
        self.grid.append([0 for _ in range(self.w)])

    def append_culomn(self):
        self.w += 1
        for row in self.grid:
            row.append(0)

class Buffer(object):
    def __init__(self, matrix):
        """
        type matrix: list[list]
        """
        self.height = len(matrix)
        if not self.height:
            return
        self.width = len(matrix[0])
        if not self.width:
            return

        quadrant_tl = Quadrant(self.width // 2, self.height // 2)
        quadrant_tr = Quadrant(self.width - self.width // 2. self.height // 2)
        quadrant_bl = Quadrant(self.width // 2, self.height - self.height // 2)
        quadrant_br = Quadrant(self.width - self.width // 2,
                self.height - self.height // 2)
