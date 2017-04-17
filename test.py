# -*- coding: utf-8 -*-

import evdev
import os
import select
import sys

if __name__ == '__main__':
    if os.geteuid():
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)
