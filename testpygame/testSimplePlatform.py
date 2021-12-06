import math, os, random, sys
import pygame

#imports me
import configurations as config
import engine.thing as engine
import engine.collider as collider

import initThingGame as initTG
import gamelogic as gamelogic

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
# player.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'object1.png'))
player.initThingBasic(config.screenWidth/2 - 50, config.screenHeight-120, 60, 30, 'object1.png', 5)
initTG.initThingPlayer(player)
initTG.initThingCanJump(player, player.height + 30)
# player.SetRectCollider(5, 20, 50)
player.SetRectCollider(20, 50, 5)

#define dummys
dy = config.screenHeight-120
dummy01 = engine.Thing("dummy01")
# dummy01.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'dummy01.png'))
dummy01.initThingBasic(config.screenWidth - 200, dy, 60, 30, 'dummy01.png', 5, 2)
dummy01.SetRectCollider(5, 20, 50)

dummy02 = engine.Thing("dummy02")
dummy02.initThingBasic(100, dy, 60, 30, dummy01.image, 5, 2)
dummy02.SetRectCollider(5, 20, 50)

dummys = [dummy01, dummy02]

#define bullet
imgBullet01 = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', 'bullet01.png'))
bullets = []

#define solid surfaces
surface1 = engine.Thing("srufaceV01")
surface1.image = dummy01.image
surface1.initThingBasic(config.screenWidth-50, dy, 60, 30, dummy01.image, 0, 4)
initTG.initThingSurfaceV(surface1, 1)

#functions
def init_game_data():
    global bullets
    global player
    
    for i in range(player.munition):
        bullets.append(engine.Thing("bullet0" + str(i)))
        bullets[i].initThingBasic(-100, -100, 10, 20, imgBullet01, 20, 3)
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
    canvas.blit(surface1.image, (surface1.postX, surface1.postY))

    for item in bullets:
        if(item.isMoving):
            canvas.blit(imgBullet01, (item.postX, item.postY))

def PressDownKey(eventType):
    global player, running    
    if eventType == pygame.K_ESCAPE:
        running = False
    elif eventType == pygame.K_RIGHT:
        player.directionX = 1
        player.isMoving = True
    elif eventType == pygame.K_LEFT:
        player.directionX = -1
        player.isMoving = True
    elif eventType == pygame.K_UP:
        player.isJump = True
        player.directionY = -1
    elif eventType == pygame.K_SPACE:        
        if(not player.isShooting):            
            player.isShooting = True
            # for item in bullets:
            #     print(item.name, item.isMoving)
    elif eventType == pygame.K_l:
        print("clear")
        print("-------------------------")
            

def PressKey(pressed):
    global running
    #opcion para dejar presionado tecla, es mas suave al cambio de la tecla
    if pressed[pygame.K_ESCAPE]:
        running = False    
    elif pressed[pygame.K_RIGHT] == 1:
        player.directionX = 1
        player.isMoving = True
    elif pressed[pygame.K_LEFT] == 1:
        player.directionX = -1
        player.isMoving = True
    elif pressed[pygame.K_UP]:
        player.isJump = True
        player.directionY = -1
    elif pressed[pygame.K_SPACE]:        
        if(not player.isShooting):            
            player.isShooting = True

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
            PressDownKey(event.key)
            
        elif event.type == pygame.KEYUP:            
            if event.key == pygame.K_RIGHT:
                if(pygame.key.get_pressed()[pygame.K_LEFT] != 1):
                    player.isMoving = False
            elif event.key == pygame.K_LEFT:
                if(pygame.key.get_pressed()[pygame.K_RIGHT] != 1):
                    player.isMoving = False
            # player.isMoving = False
            # player.isShooting = False

def update_screen():
    global time
    pygame.display.update()
    config.gameFPSClock.tick(config.GAME_FPS)
    time = (time + 1, 0)[time >= 61]

#init call functions
init_game_data()
draw_init(screen)

def CollisionSurfaceSquare(resCollision, surface):
    if(resCollision[0][0] and resCollision[0][1]):
        player.changeY = surface1.postY - player.height - 1
        player.iniPostY = player.changeY
    elif(resCollision[0][0] and not resCollision[0][1]):
        if(resCollision[1][0]):
            player.changeX = surface1.postX - surface1.width - 1
        elif(resCollision[1][1]):
            player.changeX = surface1.postX + surface1.width + 1

#calculations
def game_logic():
    global bullets, time
    global dummys
    global player
    global surface1
    # print('game_logic')

    # player.changeX = player.postX
    if(player.isMoving):
        player.changeX = player.postX + (player.speed*player.directionX)
        # print(player.postX, player.changeX)        

    if(player.isJump):        
        player.changeY += 5*(player.directionY) #up decrement position in y, -1 is for direction is up
        # if player.changeY <= ((initTG.INI_POST_Y - player.limitJump) + 10):
        # print("player.changeY", player.changeY, "player.limitJump", player.limitJump, "player.posInitJump", player.posInitJump,
        #      (player.posInitJump - player.limitJump))
        if((player.changeY + player.height) <= (player.posInitJump - player.limitJump)): # + 10):
            player.directionY = 1
        elif (player.changeY + player.height) >= player.posInitJump: #initTG.INI_POST_Y:
            player.changeY = player.posInitJump - player.height #initTG.INI_POST_Y
            player.isJump = False
            player.directionY = -1

    CollisionSurfaceSquare(collider.ColliderSurfaceForUp(surface1, player), surface1)


        
        # print('collision with surface', player.postX, player.changeX)

    #collider section
    for i in range(0,len(dummys)):
        # _isCollision = collider.RectangleCollision(player.postX+5, player.postY+5, 20, 50, 
        #             dummys[i].postX+5, dummys[i].postY+5, 20, 50)
        
        _isCollision = collider.RectangleCollisionThing(player, dummys[i])
        #si es en especifico, seria identificar dentro del ciclo la colisión
        if _isCollision:            
            print('collisión ----')
            if(dummys[i].type == 2):
                player.isInterfere = True

        for item in bullets:
            # _isCollision = collider.RectangleCollision(dummys[i].postX+5, dummys[i].postY+5, 20, 50, 
            #         item.postX+1, item.postY+1, 19, 9)
            _isCollision = collider.RectangleCollisionThing(item, dummys[i])
            # _isCollision = collider.RectangleCollisionThing(dummys[i], item)
            if _isCollision:
                print('colision with bullet ----')
                print('bullet: ', item.name, item.postX, item.postY, item.collider.width, item.collider.height
                    , dummys[i].postX, dummys[i].postY, dummys[i].collider.width, dummys[i].collider.height)

    for item in bullets:
        if(item.isMoving):
            item.postX = item.postX + (item.directionX*(item.speed - item.decreseSpeed))
            if(time%3 == 0):
                item.decreseSpeed = (item.decreseSpeed + 1, 15)[item.decreseSpeed >= 15]
            # print(time, time%3)
        
        if(player.isShooting and not item.isMoving):        
            #for item in bullets:
            print(item.name, item.isMoving, item.postX)
            if(item.postX == -100):
                initTG.initMoveBullet(item, player.postX, player.postY, player.directionX)
                item.isMoving = True            
                player.isShooting = False #the player already shoot

        if(config.screenWidth + 5 < item.postX or -5 > item.postX):
            if(item.postX != -100):
                print(item.name)
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

    # if(not player.isInterfere):
    #     player.postX = player.changeX

    player.postX = player.changeX
    player.postY = player.changeY
    # print(player.postX)

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    # gamelogic.GameLogic(bullets, time, dummys, player)
    update_screen()

print(config.PATH_RES_IMG)

pygame.quit()
sys.exit()