# -*- coding: utf-8 -*-

import evdev
import os
import select
import sys

def detectInputKey():
    dev = evdev.InputDevice('/dev/input/event0')
    while True:
        select.select([dev], [], [])
        for event in dev.read():
            if (event.value == 1 or event.value == 0) and event.code != 0:
                print("Key: %s Status: %s" % (event.code, "pressed" if event.value else "release"))

def haha():
    print(os.getpid())
    #dev = evdev.InputDevice('/dev/input/event10')
    dev = evdev.InputDevice('/dev/input/by-path/pci-0000:00:1d.0-usb-0:1.5:1.2-event-kbd')
    epoll = select.epoll()
    epoll.register(dev.fileno(), select.EPOLLIN)
    try:
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if event & select.EPOLLIN:
                    for e in dev.read():
                        if (e.value == 1):
                            print('e = %s, code = %s' % (e, e.code))
    finally:
        epoll.unregister(dev.fileno())
        epoll.close()

if __name__ == '__main__':
    ##detectInputKey()
    print(os.getpid())
    if os.geteuid():
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)
    haha()
