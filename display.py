# -*- coding: utf-8 -*-

import sys

from logic import Space
from logic import (
        DIE,
        LIVE,
        D_2_L,
        L_2_D,
        )

def move_mouse(x, y):
    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
    sys.stdout.write('\033[0m')

def light(x, y, s):
    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
    sys.stdout.write('\033[47m')
    sys.stdout.write(s)
    sys.stdout.write('\033[0m')

def default(x, y, s):
    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
    sys.stdout.write('\033[0m')
    sys.stdout.write(s)


class Window(object):
    space = Space()

    def __init__(self, start_x, start_y, height, width):
        self.start_x = start_x
        self.start_y = start_y
        self.height = height
        self.width = width

        self.x0 = 0
        self.y0 = 0

    def load(self, t):
        for x, y in t:
            self.space[x][y] = LIVE
            self.space.live_set.add((x, y))

    def show(self, x, y):
        light(self.start_x + x, self.start_y + y, '  ')

    def hide(self, x, y):
        default(self.start_x + x, self.start_y + y, '  ')

    def move(self, x, y):
        move_mouse(self.start_x + x, self.start_y + y)

    def clean(self):
        for i in range(self.width):
            for j in range(self.height):
                self.hide(i, j)

    def init_edge(self):
        self.hide(-1, -1)
        x = self.start_x - 1
        y = self.start_y - 1
        for i in range(self.width):
            default(self.start_x + i, y, '%.2d' % ((self.x0 + i) % 100))
        for j in range(self.height):
            default(x, self.start_y + j, '%.2d' % ((self.y0 + j) % 100))

        x = self.start_x + self.width
        y = self.start_y + self.height
        for i in range(-1, self.width):
            default(self.start_x + i, y, '--')
        for j in range(-1, self.height + 3):
            default(x, self.start_y + j, ' |')

        for i in range(-1, self.width):
            self.hide(i, y)
            self.show(i, y + 1)

    def update_edge(self):
        x = self.start_x - 1
        y = self.start_y - 1
        for i in range(self.width):
            default(self.start_x + i, y, '%.2d' % ((self.x0 + i) % 100))
        for j in range(self.height):
            default(x, self.start_y + j, '%.2d' % ((self.y0 + j) % 100))

        y = self.start_y + self.height
        for i in range(-1, self.width):
            self.hide(i, y)
        self.move(0, self.height)
        print()

    def update_center(self):
        for x in range(self.x0, self.x0 + self.width):
            for y in range(self.y0, self.y0 + self.height):
                if self.space[x][y] == DIE:
                    self.hide(x - self.x0, y - self.y0)
                else:
                    self.show(x - self.x0, y - self.y0)
        self.move(0, self.height)
        print()

    def move_j(self):
        self.y0 += 1
        self.update_edge()
        self.update_center()

    def move_k(self):
        self.y0 -= 1
        self.update_edge()
        self.update_center()

    def move_h(self):
        self.x0 -= 1
        self.update_edge()
        self.update_center()

    def move_l(self):
        self.x0 += 1
        self.update_edge()
        self.update_center()

    def next_step(self):
        self.space.next_step()
        self.update_center()

def window_init():
    w = Window(1, 1, 32, 64)
    t = []
    for _ in range(256):
        x = random.randint(0, 63)
        y = random.randint(0, 31)
        t.append((x, y))
    w.load(t)
    w.clean()
    w.init_edge()
    w.update_center()

    return w


import random
import time

if __name__ == '__main__':
    #w = Window(1, 5, 32, 64)
    #t = []
    #for _ in range(256):
    #    x = random.randint(0, 63)
    #    y = random.randint(0, 31)
    #    t.append((x, y))
    #w.load(t)
    #for _ in range(34):
    #    print()
    ##light(0, 0, '  ')
    ##light(0, 2, '  ')
    ##default(2, 2, '01')
    ##default(4, 2, '05')
    ##w.hide(0, 39)

    window = window_init()
    time.sleep(1)
    window.move_h()
    time.sleep(1)
    window.move_l()

    time.sleep(1)
    window.move_j()
    time.sleep(1)
    window.move_k()

    time.sleep(1)
    window.move_l()
    time.sleep(1)
    window.move_h()

    time.sleep(1)
    window.move_k()
    time.sleep(1)
    window.move_j()

    #s = Space()
    #print(s[9][0])
    #print(s[0])
    #s[9][0] = 4
    #s[3][2] = 56
    #s[-2][4] = 5
    #print(s[9][0])
    #print(s[-2][4])
    #print(s[3][4])
    #print(s[3][2])
