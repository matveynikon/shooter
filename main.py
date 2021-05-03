import pygame
import random
import math
import time
from math import atan2, degrees, pi

pygame.init()
from pygame import mixer

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('clone war')

playerImg = pygame.image.load('player2.png')
bg = pygame.image.load('bg.png')
bul1 = pygame.image.load('bullet3.png')
bul2 = pygame.image.load('bullet3.png')
bul3 = pygame.image.load('bullet3.png')
bul4 = pygame.image.load('bullet3.png')
bul5 = pygame.image.load('bullet3.png')

speed_x = 0
speed_y = 0

a3 = 0
ku = 20
f = 0

px = 470
py = 200
pc = 0
pc2 = 0
angle = 0
angle2 = 0
ev = 0
bx = 585
by = 280

aby = py
byc = -1
fire = True

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:
    clock.tick(52)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        dx = mouse_x - px
        dy = mouse_y - py
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        a3 = degrees(rads)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pc = -2
            if event.key == pygame.K_RIGHT:
                pc = 2
            if event.key == pygame.K_UP:
                pc2 = -2
            if event.key == pygame.K_DOWN:
                pc2 = 2
            if event.key == pygame.K_SPACE:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                dx = mouse_x - px
                dy = mouse_y - py
                angle = dy / 10
                angle2 = dx / 10
                bx = px + 30
                by = py + 50
                print(angle)
                print(angle2)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_SPACE:
                pc = 0
                pc2 = 0
                bx = 1000000
                by = 1000000
                angle = 0
                angle2 = 0

    px += pc
    py += pc2
    bx += angle2
    by += angle
    pl2 = pygame.transform.rotate(playerImg, a3 - 89)
    screen.blit(bg, (0, 0))
    screen.blit(pl2, (px, py))
    screen.blit(bul1, (bx, by))

    pygame.display.update()
