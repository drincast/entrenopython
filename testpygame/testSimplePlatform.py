import math, os, random, sys
import pygame

#imports me
import configurations
#import engine.thing as engine
import engine.thing as engine
import engine.collider as collider

import initThingGame as initTG

pygame.init()

#configurations
configurations.gameFPSClock = pygame.time.Clock()
time = 0
running = True

#colors
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
BLACK = (0,0,0)

#create of screen
#size, flag= 0 (pygame.NOFRAME), depth, display, vsync
screen = pygame.display.set_mode((configurations.screenWidth, configurations.screenHeight))
pygame.display.set_caption('SimplePlatform')

#define entities, object, things of the game
player = engine.Thing("player1")
player.image = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'test', 'object1.png'))
initTG.initThingPlayer(player)

#define dummys
dy = configurations.screenHeight-120
dummy01 = engine.Thing("dummy01")
dummy01.image = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'test', 'dummy01.png'))
initTG.initThingDummy(dummy01, configurations.screenWidth - 200, dy)

dummy02 = engine.Thing("dummy02")
dummy02.image = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'test', 'dummy01.png'))
initTG.initThingDummy(dummy02, 100, dy)

dummys = [dummy01, dummy02]

#functions
def init_game_data():
    print('init_game_data')

def drawDummys(canvas):
    global dummys
    for i in range(0,len(dummys)):
        canvas.blit(dummys[i].image, (dummys[i].postX, dummys[i].postY))

def draw_init(canvas):
    print('draw_init')
    canvas.fill(BLACK)

def draw(canvas):
    global dummy01
    global player
    canvas.fill(BLACK)
    drawDummys(canvas)
    canvas.blit(player.image, (player.postX, player.postY))
    pygame.draw.circle(canvas, BLUE, (player.postX+5, player.postY+5), 3, 0)
    pygame.draw.rect(canvas, RED, (dummy01.postX+5, dummy01.postY+5, 20, 50), 1)

def PressDownKey(eventType):
    global player, running    
    if eventType == pygame.K_ESCAPE:
        running = False
    elif eventType == pygame.K_RIGHT:
        player.direction = 1
        player.isMoving = True
    elif eventType == pygame.K_LEFT:
        player.direction = -1
        player.isMoving = True

def PressKey(pressed):
    #opcion para dejar presionado tecla, es mas suave al cambio de la tecla
    if pressed[pygame.K_ESCAPE]:
        running = False    
    elif pressed[pygame.K_RIGHT] == 1:
        player.direction = 1
        player.isMoving = True
    elif pressed[pygame.K_LEFT] == 1:
        player.direction = -1
        player.isMoving = True

def handle_input():
    global running
    global player
    for event in pygame.event.get():
        # print('-->')
        # print(pygame.key.get_repeat()) 
        #PressKey(pygame.key.get_pressed())
        if event.type == pygame.QUIT:
            print('event QUIT')
            running = False
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_ESCAPE:
            #     running = False
            # elif event.key == pygame.K_RIGHT:
            #     player.direction = 1
            #     player.isMoving = True
            # elif event.key == pygame.K_LEFT:
            #     player.direction = -1
            #     player.isMoving = True
            PressDownKey(event.key)
            
            
        elif event.type == pygame.KEYUP:
            player.isMoving = False    

def update_screen():
    pygame.display.update()
    configurations.gameFPSClock.tick(configurations.GAME_FPS)

#init call functions
init_game_data()
draw_init(screen)

#calculations
def game_logic():
    global dummy01, dummys
    global player
    # print('game_logic')

    if(player.isMoving):
        player.postX += player.speed*player.direction

    #collider section
    for i in range(0,len(dummys)):
        _isCollision = collider.RectangleCollision(player.postX+5, player.postY+5, 20, 50, 
                    dummys[i].postX+5, dummys[i].postY+5, 20, 50)
        #si es en especifico, seria identificar dentro del ciclo la colisión
        if _isCollision:
            print('colisión ----')
    
    

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()