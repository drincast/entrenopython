import platform, sys
import math
import random

import pygame
from pygame import mixer

import configurations

#initialize pygame
pygame.init()
#pygame.font.init()

#configurations
configurations.gameFPSClock = pygame.time.Clock()

#create the screen
screen = pygame.display.set_mode((configurations.screenWidth, configurations.screenHeight))

#load image
background = pygame.image.load(configurations.PATH_RES_IMG + '/estrella-en-el-espacio.jpg')
enemy = pygame.image.load(configurations.PATH_RES_IMG + '/enemy.png')

#load sound
# mixer.music.load(configurations.PATH_RES_SOUND + '/background.wav')
# mixer.music.play(-1)

#caption icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(configurations.PATH_RES_IMG + '/ufo.png')
pygame.display.set_icon(icon)

#text score
score_value = 0
#font = pygame.font.Font('freesansbold.ttf', 32)
#font = pygame.font.Font('/usr/share/fonts/truetype/lato/Lato-Hairline.ttf', 32)
#pygame.font.get_fonts()
textX = 10
textY = 10


#player
playerImg = pygame.image.load(configurations.PATH_RES_IMG + "/player.png")
playerX = 370
playerY = 480
playerX_change = 0

#configuration Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

#bullet
#ready - no see de bullet on the screen
#fire - the bullet it is in movement
bulletImg = pygame.image.load(configurations.PATH_RES_IMG + "/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def CreateEnemies():
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load(configurations.PATH_RES_IMG + '/enemy.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))
    
def set_font():
    so = platform.system()
    so = so.upper()
    font = None

    print(so)

    if so == 'WINDOWS':
        font = pygame.font.Font(pygame.font.match_font('inkfree'), 32)
    elif so == 'LINUX':
        font = pygame.font.Font(pygame.font.match_font('lato'), 32)

    return font    

def show_score(font):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    return score

#function for spawn the enemies ver 01
def SpawnEnemies01(xInitPositionEnemy, xEndPositionEnemy, yInitPositionEnemy, flagRow):
    #varible configuration
    # xInitPositionEnemy = 34
    # xEndPositionEnemy = 740
    # yInitPositionEnemy = 4
    # flagRow = 0
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

def fire_bullet(x, y):
    global bullet_state, bulletImg
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def set_background():
    global backgroud
    #RGB
    screen.fill((0, 0, 0))
    #put backgroud image
    screen.blit(background, (0, 0))

def game_input():
    global bullet_state, bulletX, bulletY, playerX, playerX_change, running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            elif event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound(configurations.PATH_RES_SOUND + "/laser.wav")
                    bulletSound.play()
                    # get the current x coordinate of ship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    move_playerX()

def move_playerX():
    global playerX, playerX_change

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 770:
        playerX = 770

def move_bullet():
    global bulletX, bulletY, bullet_state, bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

def enemy_movement(index):
    global enemyX, enemyY, enemyX_change, enemyY_change
    enemyX[index] += enemyX_change[index] 

    if enemyX[index] <= 0:
        enemyX_change[index] = 4
        enemyY[index] += enemyY_change[index]
    elif enemyX[index] >= 750:
        enemyX_change[index] = -4
        enemyY[index] += enemyY_change[index]

    enemy(enemyX[index], enemyY[index], index)

def enemy_collision(index):
    #collision
    global configurations, bulletY, bulletX, bullet_state, enemyX, enemyY, score_value
    collision = isCollision(enemyX[index], enemyY[index], bulletX, bulletY)
    if collision:
        explosionSound = mixer.Sound(configurations.PATH_RES_SOUND + "/explosion.wav")
        explosionSound.set_volume(0.5)
        explosionSound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX[index] = random.randint(0, 736)
        enemyY[index] = random.randint(50, 150)

font = set_font()
running = True

while running:
    set_background()            

    # SpawnEnemies01(34, 740, 4, 0)
    CreateEnemies()
    game_input()
    #move_playerX()

    move_bullet()

    #enemy movement
    for i in range(num_of_enemies):
        enemy_movement(i)
        enemy_collision(i)       

    screen.blit(show_score(font), (10, 10))    

    player(playerX, playerY)
    pygame.display.update()
    configurations.gameFPSClock.tick(configurations.GAME_FPS)

