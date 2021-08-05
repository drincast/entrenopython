import pygame
#from pygame import mixer

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#load image
background = pygame.image.load('res\img\estrella-en-el-espacio.jpg')
enemy = pygame.image.load('res\img\enemy.png')

#varible configuration
xInitPositionEnemy = 34
xEndPositionEnemy = 740
yInitPositionEnemy = 4
flagRow = 0

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

    pygame.display.update()

