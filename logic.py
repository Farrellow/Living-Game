# -*- coding: utf-8 -*-

import sys

DIE   = 0
LIVE  = 1
D_2_L = 2
L_2_D = 3


class Space(object):
    # space[x][y] -> int, x and y can be any int
    #
    # scale_d: tuple(i, j) -> list[list[]]                                   
    #
    # for any i, j:
    # there is a block = scale_d[(i, j)], that:
    # x == i * scale + x0 and y == j * scale + y0
    # <==> space[x][y] is block[x0][y0]
    scale = 5
    live_set = set()  # (x, y)

    class Block(list):
        def __init__(self):
            list.__init__(self)
            for _ in range(Space.scale):
                self.append([DIE for _ in range(Space.scale)])

    scale_d = {}  # (i, j) -> Block

    class L(list):
        def __init__(self, x):
            self.x = x
            self.i = x // Space.scale
    
        def __getitem__(self, y):
            j = y // Space.scale
            if Space.scale_d.get((self.i, j)) == None:
                return 0
            else:
                block = Space.scale_d[(self.i, j)]
                return block[self.x % Space.scale][y % Space.scale]

        def __setitem__(self, y, val):
            j = y // Space.scale
            if Space.scale_d.get((self.i, j)) == None:
                block = Space.Block()
                block[self.x % Space.scale][y % Space.scale] = val
                Space.scale_d[(self.i, j)] = block
            else:
                block = Space.scale_d[(self.i, j)]
                block[self.x % Space.scale][y % Space.scale] = val

    def __init__(self):
        self.x_d = {} # x -> L

    def __getitem__(self, x):
        if self.x_d.get(x) == None:
            self.x_d[x] = self.L(x)
            return self.x_d[x]
        else:
            return self.x_d[x]

    def get_neighbors(self, x, y):
        return [
                (i, j) for i in range(x - 1, x + 2) 
                    for j in range(y - 1, y + 2) 
                        if x != i or y != j
                ]

    def next_step(self):
        handlered_set = set()
        to_del_set = set()
        to_add_set = set()
        for x, y in self.live_set:
            neighbors = self.get_neighbors(x, y)
            count = 0
            for xx, yy in neighbors:
                if self[xx][yy] == LIVE or self[xx][yy] == L_2_D:
                    count += 1
            if count == 2 or count == 3:
                pass
            else:
                self[x][y] == L_2_D
                to_del_set.add((x, y))

            for xx, yy in neighbors:
                if (xx, yy) in self.live_set:
                    continue
                if (xx, yy) in handlered_set:
                    continue
                neighbors_2 = self.get_neighbors(xx, yy)
                neighbors_count = 0
                for xxx, yyy in neighbors_2:
                    if self[xxx][yyy] == LIVE or self[xxx][yyy] == L_2_D:
                        neighbors_count += 1
                if neighbors_count == 3:
                    self[xx][yy] == D_2_L
                    to_add_set.add((xx, yy))
                handlered_set.add((xx, yy))

        for x, y in to_del_set:
            self[x][y] = DIE
            self.live_set.discard((x, y))
        for x, y in to_add_set:
            self[x][y] = LIVE
            self.live_set.add((x, y))
