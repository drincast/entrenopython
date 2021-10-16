import math, os, random, sys
import pygame

#imports me
import configurations
#import engine.thing as engine
import engine.thing as engine
import engine.collider as collider

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
player.postX = configurations.screenWidth/2 - 50
player.postY = configurations.screenHeight-120
player.speed = 5
player.direction = 1
player.isMoving = False

#functions
def init_game_data():
    print('init_game_data')

def draw_init(canvas):
    print('draw_init')
    canvas.fill(BLACK)

def draw(canvas):
    global player
    canvas.fill(BLACK)
    canvas.blit(player.image, (player.postX, player.postY))

def PressDownKey(eventType):
    global player
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
        print('-->')
        print(pygame.key.get_repeat())
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
            #PressDownKey(event.key)
            
            PressKey(pygame.key.get_pressed())
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
    global player
    # print('game_logic')

    if(player.isMoving):
        player.postX += player.speed*player.direction

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()