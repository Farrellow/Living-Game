# -*- coding: utf-8 -*-

import sys

from init import initialize
from logic import next_step, show_display

#if __name__ == '__main__':
#    epoll = select.epoll()
#    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
#    while True:
#        events = epoll.poll(1)
#        for fileno, event in events:
#            print('fileno = ', fileno)
#            print('event = ', event)
#            s = sys.stdin.read(1)
#            print('s = ', s)

if __name__ == '__main__':
    initialize()
    while True:
        input()
        next_step()
        show_display()
