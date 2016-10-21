# -*- coding: utf-8 -*-

import sys

from init import initialize
from logic import next_step, show_display, _print

if __name__ == '__main__':
    initialize()
    i = 0
    while True:
        input()
        next_step()
        show_display()
        i += 1
        _print(0, 0, str(i))
