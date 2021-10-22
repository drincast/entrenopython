import math, os, random, sys
import pygame

#imports me
import configurations as config
import engine.thing as engine
import engine.collider as collider

import initThingGame as initTG

pygame.init()

#configurations
config.gameFPSClock = pygame.time.Clock()
time = 0
running = True

#create of screen
#size, flag= 0 (pygame.NOFRAME), depth, display, vsync
screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))
pygame.display.set_caption('SimplePlatform')

#define entities, object, things of the game
player = engine.Thing("player1")
player.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'object1.png'))
initTG.initThingPlayer(player)
print(player)

#define dummys
dy = config.screenHeight-120
dummy01 = engine.Thing("dummy01")
dummy01.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'dummy01.png'))
initTG.initThingDummy(dummy01, config.screenWidth - 200, dy)

dummy02 = engine.Thing("dummy02")
dummy02.image = dummy01.image
#dummy02.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'dummy01.png'))
initTG.initThingDummy(dummy02, 100, dy)

dummys = [dummy01, dummy02]

#define bullet
imgBullet01 = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'bullet01.png'))
bullets = []

#functions
def init_game_data():
    global bullets
    global player
    
    for i in range(player.munition):
        bullets.append(engine.Thing("bullet0" + str(i)))
        initTG.initBullet(bullets[i])
    #print('init_game_data')

def drawDummys(canvas):
    global dummys
    for i in range(0,len(dummys)):
        canvas.blit(dummys[i].image, (dummys[i].postX, dummys[i].postY))

def draw_init(canvas):
    print('draw_init')
    canvas.fill(config.BLACK)

def draw(canvas):
    global dummy01
    global player
    canvas.fill(config.BLACK)
    drawDummys(canvas)
    canvas.blit(player.image, (player.postX, player.postY))
    pygame.draw.circle(canvas, config.BLUE, (player.postX+5, player.postY+5), 3, 0)
    pygame.draw.rect(canvas, config.RED, (dummy01.postX+5, dummy01.postY+5, 20, 50), 1)

    for item in bullets:
        if(item.isMoving):
            canvas.blit(imgBullet01, (item.postX, item.postY))

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
    elif eventType == pygame.K_UP:
        player.isJump = True
    elif eventType == pygame.K_SPACE:        
        if(not player.isShooting):            
            player.isShooting = True
            # for item in bullets:
            #     print(item.name, item.isMoving)

def PressKey(pressed):
    global running
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
            player.isShooting = False

def update_screen():
    global time
    pygame.display.update()
    config.gameFPSClock.tick(config.GAME_FPS)
    time = (time + 1, 0)[time >= 61]
    


#init call functions
init_game_data()
draw_init(screen)

#calculations
def game_logic():
    global bullets, time
    global dummy01, dummys
    global player
    # print('game_logic')

    if(player.isMoving):
        player.postX += player.speed*player.direction

    if(player.isJump):
        player.postY += 5*(player.directionY) #up decrement position in y, -1 is for direction is up
        if player.postY <= ((initTG.INI_POST_Y - player.limitJump) + 10):
            player.directionY = 1
        elif player.postY >= initTG.INI_POST_Y:
            player.postY = initTG.INI_POST_Y
            player.isJump = False
            player.directionY = -1

    #collider section
    for i in range(0,len(dummys)):
        _isCollision = collider.RectangleCollision(player.postX+5, player.postY+5, 20, 50, 
                    dummys[i].postX+5, dummys[i].postY+5, 20, 50)
        #si es en especifico, seria identificar dentro del ciclo la colisión
        if _isCollision:
            print('colisión ----')

        for item in bullets:
            _isCollision = collider.RectangleCollision(dummys[i].postX+5, dummys[i].postY+5, 20, 50, 
                    item.postX+1, item.postY+1, 19, 9)
            if _isCollision:
                print('colision with bullet ----')
                

    for item in bullets:
        if(item.isMoving):
            item.postX = item.postX + (item.direction*(item.speed - item.decreseSpeed))
            if(time%3 == 0):
                item.decreseSpeed = (item.decreseSpeed + 1, 15)[item.decreseSpeed >= 15]
            print(time, time%3)
        
        #este es el problema analizar bien para que se ejecuten las otras bullets
        if(player.isShooting and not item.isMoving):        
            #for item in bullets:
            print(item.name, item.isMoving, item.postX)
            if(item.postX == -100):
                initTG.initMoveBullet(item, player.postX, player.postY, player.direction)
                item.isMoving = True            
                player.isShooting = False

        if(config.screenWidth + 5 < item.postX or -5 > item.postX):
            if(item.postX != -100):
                print(item.name)
                print(bullets)
            item.postX = -100
            item.isMoving = False        

        # if(len(bullets) <= 0):
        #     bullets.append(engine.Thing("bullet01"))
        # else:
        #     if(len(bullets) <= 3):
        #         bullets.append(engine.Thing("bullet0" + str(len(bullets)-1)))
        #     else:
        #         for item in bullets:
        #             if(item.postX == -100):
        #                 initTG.initBullet(item, player.postX, player.postY, player.direction)
        #                 item.isMoving = True

    #recorrido de bullets para movimiento de bullets


#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(config.PATH_RES_IMG)

pygame.quit()
sys.exit()