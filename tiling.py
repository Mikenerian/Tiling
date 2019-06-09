# -*- coding: utf-8 -*-
# タイリングを考えるプログラム

import numpy as np

tiles = np.random.randint(2, size=(4,5))


for i in range(tiles.shape[0]-1):
    for j in range(tiles.shape[1]-1):
        if tiles[i,j] == 0:
            tiles[i+1,j] = 1
            tiles[i,j+1] = 1
        else:
            tiles[i+1,j] = 0
            tiles[i,j+1] = 0

# 一番最後の値のみ、上のプログラムだと反映されないため追記
if tiles[tiles.shape[0]-2,tiles.shape[1]-1] == 0:
    tiles[tiles.shape[0]-1,tiles.shape[1]-1] = 1
else:
    tiles[tiles.shape[0]-1,tiles.shape[1]-1] = 0


print(tiles)
