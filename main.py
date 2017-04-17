# -*- coding: utf-8 -*-

import sys

from init import initialize, randan_init
from logic import next_step, show_display, _print

if __name__ == '__main__':
    #initialize()
    randan_init()
    i = 0
    while True:
        input()
        next_step()
        show_display()
        i += 1
        _print(0, 0, str(i))
