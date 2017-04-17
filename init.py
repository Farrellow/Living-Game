# -*- coding: utf-8 -*-

import random

from logic import cell_space, x_axis_end, y_axis_end

def randan_init():
    for i in range(x_axis_end):
        for j in range(y_axis_end):
            if random.randint(1, 3) == 3:
                cell_space[i][j] = 3

def initialize():
    cell_space[27][13] = 3

    cell_space[28][13] = 3
    cell_space[28][14] = 3
    cell_space[28][15] = 3
    cell_space[28][16] = 3
                  
    cell_space[29][13] = 3
    cell_space[29][15] = 3
                  
    cell_space[30][13] = 3
    cell_space[30][14] = 3
    cell_space[30][15] = 3

    cell_space[31][14] = 3
    cell_space[31][15] = 3
    cell_space[31][16] = 3
    cell_space[31][17] = 3

    cell_space[21][12] = 3
    cell_space[21][13] = 3
    cell_space[21][14] = 3
    cell_space[21][15] = 3

    cell_space[25][14] = 3
    cell_space[25][15] = 3
    cell_space[25][16] = 3
    cell_space[25][17] = 3

    cell_space[26][16] = 3
    cell_space[26][17] = 3
