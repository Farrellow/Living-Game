# -*- coding: utf-8 -*-

import sys

from init import initialize
from logic import next_step, show_display

if __name__ == '__main__':
    initialize()
    while True:
        input()
        next_step()
        show_display()
