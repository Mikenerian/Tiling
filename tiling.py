# -*- coding: utf-8 -*-
# タイリングを考えるプログラム

import numpy as np
import random

colors = 3
tiles = np.random.randint(colors, size=(5,5))
counter = 0

for i in range(1, tiles.shape[0]):
    while not(tiles[i,0] != tiles[i-1,0]):
        tiles[i,0] = random.randint(0, colors-1)

for j in range(1, tiles.shape[1]):
    while not(tiles[0,j] != tiles[0,j-1]):
        tiles[0,j] = random.randint(0, colors-1)

for i in range(1, tiles.shape[0]):
    for j in range(1,tiles.shape[1]):
        while not(tiles[i,j] != tiles[i-1,j] and tiles[i,j] != tiles[i,j-1]):
            tiles[i,j] = random.randint(0, colors-1)
            counter += 1

print(tiles)
print(counter)
