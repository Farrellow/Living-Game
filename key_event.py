# -*- coding: utf-8 -*-

import evdev
import os
import select
import struct

class KeyboardEventListen(object):
    def __init__(self):
        self.file_fd = {}
        self.epoll = select.epoll()
        self.s_set = set([
            35,  # h
            36,  # j
            37,  # k
            38,  # l
            28,  # Enter
            ])
        self.prev_code = 0

        in_device = os.listdir('/dev/input/by-path')
        for device in in_device:
            if 'kbd' in device:
                path = os.path.join('/dev/input/by-path', device)
                dev = evdev.InputDevice(path)
                self.file_fd[dev.fileno()] = dev
                self.epoll.register(dev.fileno(), select.EPOLLIN)

    def listening(self):
        with open('kbd_fifo', 'wb') as f:
            f.write(b'b')  # begin
            f.flush()
            try:
                while True:
                    events = self.epoll.poll(1)
                    for fileno, event in events:
                        if event & select.EPOLLIN:
                            for e in self.file_fd[fileno].read():
                                if (e.value == 1):
                                    self.event_handler(f, e.code)
            finally:
                for fileno, dev in self.file_fd.items():
                    self.epoll.unregister(fileno)
                self.epoll.close()

    def event_handler(self, f, code):
        if code in self.s_set:
            b = struct.pack('>B', code)
            f.write(b)
            f.flush()
            self.prev_code = code
        else:
            if code == 0:
                if self.prev_code in self.s_set:
                    b = struct.pack('>B', self.prev_code)
                    f.write(b)
                    f.flush()
                else:
                    pass
            else:
                self.prev_code = code

if __name__ == '__main__':
    # 1.init keyboard event listen
    # 2.open fifo file with write mode
    # 3.send data to parent process when keyboard event happen
    keyboard_event = KeyboardEventListen()
    keyboard_event.listening()
