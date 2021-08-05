import math
import random

import pygame
from pygame import mixer

#CONSTANTS
PATH_RES_IMG = "res/img"
PATH_RES_SOUND = 'res/sound'

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#load image
background = pygame.image.load(PATH_RES_IMG + '/estrella-en-el-espacio.jpg')
enemy = pygame.image.load('res/img/enemy.png')

#load sound
mixer.music.load('res/sound/background.wav')
mixer.music.play(-1)

#caption icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(PATH_RES_IMG + '/ufo.png')
pygame.display.set_icon(icon)

#text score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


#player
playerImg = pygame.image.load(PATH_RES_IMG + "/player.png")
playerX = 370
playerY = 480
playerX_change = 0

#varible configuration
xInitPositionEnemy = 34
xEndPositionEnemy = 740
yInitPositionEnemy = 4
flagRow = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))

#function for spawn the enemies ver 01
def SpawnEnemies01(xInitPositionEnemy, xEndPositionEnemy, yInitPositionEnemy, flagRow):
    for y in range(yInitPositionEnemy, 272, 72):
        for x in range(xInitPositionEnemy, xEndPositionEnemy, 74):
            screen.blit(enemy, (x, y))

        flagRow += 1
        
        if xInitPositionEnemy == 34 and flagRow%2 != 0:
            xInitPositionEnemy = 68
            xEndPositionEnemy = 676
        else:
            xInitPositionEnemy = 34
            xEndPositionEnemy = 740   


running = True
while running:
    #RGB
    screen.fill((0, 0, 0))

    #put backgroud image
    screen.blit(background, (0, 0))        

    SpawnEnemies01(34, 740, 4, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()

