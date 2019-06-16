# -*- coding: utf-8 -*-
# タイリングを考えるプログラム

import numpy as np
import random

import pygame
from pygame.locals import *
import sys

COLORS = {
'R': (234,85,50),
'RY': (246,173,60),
'Y': (255,243,63),
'YG': (170,207,82),
'G': (0,169,95),
'GC': (0,173,169),
'C': (0,175,236),
'CB': (24,127,196),
'B': (77,67,152),
'BM': (166,74,151),
'M': (232,82,152),
'MR': (233,84,107)
}

color_num = 8
tile_width = 10
tile_height = 6

colors = []
for value in COLORS.values():
    colors.append(value)
colors = colors[:color_num]
colors.append([COLORS.values()])
tiles = np.random.randint(color_num, size=(tile_height, tile_width))
counter = 0

for i in range(1, tile_height):
    while not(tiles[i,0] != tiles[i-1,0]):
        tiles[i,0] = random.randint(0, color_num-1)

for j in range(1, tile_width):
    while not(tiles[0,j] != tiles[0,j-1]):
        tiles[0,j] = random.randint(0, color_num-1)

for i in range(1, tile_height):
    for j in range(1,tile_width):
        while not(tiles[i,j] != tiles[i-1,j] and tiles[i,j] != tiles[i,j-1]):
            tiles[i,j] = random.randint(0, color_num-1)
            counter += 1

print(tiles)
print(counter)
print(colors)

pygame.init()
screen_width = 600
screen_height = round(600*tile_height/tile_width)
screen = pygame.display.set_mode([screen_width, screen_height])
while True:
    screen.fill((255,255,255))
    for i in range(tile_height):
        for j in range(tile_width):
            color = tiles[i][j]
            pygame.draw.rect(screen, colors[color], Rect(j*screen_width/tile_width, i*screen_width/tile_width, screen_width/tile_width, screen_height/tile_height))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:  # 終了イベント
            sys.exit()
