# -*- coding: utf-8 -*-

import sys

x_axis_start = 0
x_axis_end   = 60
y_axis_start = 0
y_axis_end   = 30

L = 1
L_2_D = 2
D_2_L = 3
D = 0

cell_space = {
        i: {
                j: 0 for j in range(y_axis_start, y_axis_end)
                } for i in range(x_axis_start, x_axis_end)
        }

def show(x, y):
    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
    sys.stdout.write('\033[47m')
    sys.stdout.write('  ')
    sys.stdout.write('\033[0m')

def hide(x, y):
    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
    sys.stdout.write('\033[0m')
    sys.stdout.write('  ')

def show_display():
    for i in range(x_axis_end):
        for j in range(y_axis_end):
            if cell_space[i][j] == D_2_L:
                cell_space[i][j] = L
                show(i, j)
            if cell_space[i][j] == L_2_D:
                cell_space[i][j] = D
                hide(i, j)

def get_count(i, j):
    count = 0
    if i > 0:
        if cell_space[i - 1][j] == L or cell_space[i - 1][j] == L_2_D:
            count += 1
    if i < x_axis_end - 1:
        if cell_space[i + 1][j] == L or cell_space[i + 1][j] == L_2_D:
            count += 1
    if j > 0:
        if cell_space[i][j - 1] == L or cell_space[i][j - 1] == L_2_D:
            count += 1
    if j < y_axis_end - 1:
        if cell_space[i][j + 1] == L or cell_space[i][j + 1] == L_2_D:
            count += 1

    if i > 0 and j > 0:
        if cell_space[i - 1][j - 1] == L or cell_space[i - 1][j - 1] == L_2_D:
            count += 1
    if i > 0 and j < y_axis_end - 1:
        if cell_space[i - 1][j + 1] == L or cell_space[i - 1][j + 1] == L_2_D:
            count += 1
    if i < x_axis_end - 1 and j > 0:
        if cell_space[i + 1][j - 1] == L or cell_space[i + 1][j - 1] == L_2_D:
            count += 1
    if i < x_axis_end - 1 and j < y_axis_end - 1:
        if cell_space[i + 1][j + 1] == L or cell_space[i + 1][j + 1] == L_2_D:
            count += 1

    return count

def next_step():
    for i in range(x_axis_end):
        for j in range(y_axis_end):
            count = get_count(i, j)
            status = cell_space[i][j]
            if status == L:
                if count < 2:
                    cell_space[i][j] = L_2_D
                elif count > 3:
                    cell_space[i][j] = L_2_D
                else:
                    pass
            if status == D:
                if count == 3:
                    cell_space[i][j] = D_2_L
