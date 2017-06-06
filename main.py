# -*- coding: utf-8 -*-

import os
import random
import socket
import struct
import sys
import time

from display import Window

def maingg():
    port = 10000
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(4)
        client, address = sock.accept()
        while True:
            b = client.recv(1)
            i = struct.unpack('>B', b)[0]
            if i == 35:    # h
                print(i)
            elif i == 36:  # j
                print(i)
            elif i == 37:  # k
                print(i)
            elif i == 38:  # l
                print(i)
            elif i == 28:  # Enter
                print(i)
            elif i == 0:   # continuous
                print(i)
            else:          # others
                pass
    except KeyboardInterrupt as e:
        print('KeyboardInterrupt: %s' % e)
    except Exception as e:
        print('Exception: %s' % e)
    finally:
        client.close()
        sock.close()

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
        while True:
            b = f.read(1)
            if b:
                code = struct.unpack('>B', b)[0]
                print('code = %s' % code)
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
