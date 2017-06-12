# -*- coding: utf-8 -*-

import os
import random
import struct

from display import Window, window_init

def create_fifofile(path):
    try:
        os.mkfifo(path, 0o777)
    except:
        pass

def main_process():
    # 1.display init
    # 2.open fifo file with read mode
    # 3.while True: handler receive to change display

    with open('kbd_fifo', 'rb') as f:
        b = f.read(1)  # begin
        w = window_init()

        while True:
            b = f.read(1)
            if b:
                code = struct.unpack('>B', b)[0]
                if code == 35:    # h
                    w.move_h()
                elif code == 36:  # j
                    w.move_j()
                elif code == 37:  # k
                    w.move_k()
                elif code == 38:  # l
                    w.move_l()
                elif code == 28:  # Enter
                    w.next_step()
                else:             # other impossible
                    pass
            else:
                break

def main():
    create_fifofile('kbd_fifo')
    pid = os.fork()
    if pid > 0:
        # parent process
        main_process()
    elif pid == 0:
        # child process
        os.execlp('sudo', 'sudo', 'python3', 'key_event.py')
    else:
        print('error')

if __name__ == '__main__':
    main()
