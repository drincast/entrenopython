#archivo para pasar el codigo de asteroids_eng y cambiarlo a la aforma de usar el engine.
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
pygame.display.set_caption('Asteroids')

#load general images
bg = pygame.image.load(configurations.PATH_RES_IMG + '/asteroids/bg.jpg')
debris = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'debris2_brown.png'))

#definition of game objects
#the player - ship
ship = engine.Thing("ship")
ship.angle = 0
ship.direction = -1
ship.image = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'ship.png'))
ship.is_rotating = False
ship.is_forward = False
ship.postX = configurations.screenWidth/2 - 50
ship.postY = configurations.screenHeight/2 - 50
ship.speed = 0

#thrusred of ship
thrusted = engine.Thing('thrusted') 
thrusted.image = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'ship_thrusted.png'))

#the asteroids
#generic
asteroid_amount = random.randint(1, 2)
asteroidImg = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'asteroid.png'))
asteroid = []
clAsteroid = collider.Rectangle(75, 75)

#the bullets
bulletImg = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'shot2.png'))
bullet_number = 0
bullet_speed = 5
bullets = []
clBullet = collider.Rectangle(10, 10)

#varibles of tested
pressedKey = False

#functions
# functions load init
def init_game_data():
    global asteroid_amount
    #asteroids random position 
    for i in range(0, asteroid_amount):
        asteroid.append(engine.Thing("asteroid"))
        asteroid[i].image = asteroidImg
        asteroid[i].postX = random.randint(0, configurations.screenWidth)
        asteroid[i].postY = random.randint(0, configurations.screenHeight)
        asteroid[i].angle = random.randint(0, 365)
        asteroid[i].speed = random.randint(0, 6)
        
def draw_init(canvas):
    canvas.fill(BLACK)

#Convert the angle with minor values 360 or greater 360 to values in the range of 360 degrees
def transformAngleTo360(angle):
    trueAngle = (360 + angle)
    if trueAngle >= 0:
        if trueAngle >= 360:
            trueAngle = trueAngle - 360
            if trueAngle >= 360:
                trueAngle = trueAngle - 360
            #print("trueAngle: " + str(trueAngle))
        angle = trueAngle
    #print("angle: " + str(angle) + " - trueAngle: " + str(trueAngle))
    return angle

def transforAngle_0To1_forY(angle):
    value = 0
    if angle <= 90: #quadrant of 90 degrees
        value = 0
    elif angle <= 180: #quadrant of 180 degrees
        angle = 180 - (angle)
    elif angle <= 270: #quadrant of 270 degrees
        angle = -(angle - 180)
    elif angle <= 360: #quadrant of 360 degrees
        angle = -(360 - angle)

    value = angle / (-90) #quadrant of 90 degrees

    return value

def transforAngle_0To1_forX(angle):
    value = 0
    if angle <= 90: #quadrant of 90 degrees
        angle = -(90 - angle)
    elif angle <= 180: #quadrant of 180 degrees
        angle = angle - 90
    elif angle <= 270: #quadrant of 270 degrees
        angle = 270 - angle
    elif angle <= 360: #quadrant of 360 degrees
        angle = -(angle - 270)

    value = angle / (-90) #quadrant of 90 degrees

    return value
    
#rotate de ship
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    # rot_rect = orig_rect.copy()
    # rot_rect.center = rot_image.get_rect().center
    # rot_image = rot_image.subsurface(rot_rect).copy()
    orig_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(orig_rect).copy()
    # print("posx: " + str(angle))
    return rot_image

#draw game functions
def draw(canvas):
    global bg, debris, time, running
    global asteroid, asteroid_amount
    global bullets, bullet_number
    global ship
    posx = time*.3    
    canvas.blit(bg, (0,0))
    canvas.blit(debris, (posx,0))
    canvas.blit(debris, (posx-configurations.screenWidth, 0))

    for i in range(0,asteroid_amount):
        canvas.blit(rot_center(asteroid[i].image,time), (asteroid[i].postX, asteroid[i].postY))    
    
    time = time + 1
    #canvas.blit(rot_center(ship, time), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    #canvas.blit(rot_center(ship, ship_angle), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    canvas.blit(rot_center(ship.image, ship.angle), (ship.postX, ship.postY))

    if (posx-configurations.screenWidth) >= 1:
        print("time: " + str(time) + " - posx: " + str(posx) + " - width: " + str(configurations.screenWidth))
        #running = False
        time = 0

    if ship.is_forward:
        canvas.blit(rot_center(thrusted.image, ship.angle), (ship.postX, ship.postY))
    else:
        canvas.blit(rot_center(ship.image, ship.angle), (ship.postX, ship.postY))

    for i in range(0, bullet_number):        
        canvas.blit(bullets[i].image, (bullets[i].postX,bullets[i].postY))
    
# handle inputs function
def handle_input():
    global ship
    global running, pressedKey
    global bullet_angle, bullet_number, bullet_x, bullet_y

    #opcion para dejar presionado tecla, es mas suave al cambio de la tecla
    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_LEFT] == 1:
    #     print(str(kl))
    #     print(type(kl))
    #     ship_is_rotating = True
    #     ship_direction = 1
    # elif pressed[pygame.K_RIGHT] == 1:
    #     ship_is_rotating = True
    #     ship_direction = -1

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            print('event QUIT')
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.is_rotating = True
                ship.direction = 1
            elif event.key == pygame.K_RIGHT:
                ship.is_rotating = True
                ship.direction = -1
            elif event.key == pygame.K_UP:
                ship.is_forward = True
                ship.speed = 10
            elif event.key == pygame.K_SPACE:
                bullets.append(engine.Thing('bullet'))
                index = len(bullets) - 1
                bullets[index].image = bulletImg
                bullets[index].angle = ship.angle
                bullets[index].postX = ship.postX + 45 + (25 * transforAngle_0To1_forX(bullets[index].angle))
                bullets[index].postY = ship.postY + 45 + (25 * transforAngle_0To1_forY(bullets[index].angle))
                bullet_number += 1
                pressedKey = True
        elif event.type == pygame.KEYUP:
            ship.is_rotating = False
            ship.is_forward = False
            
    if ship.is_rotating:
        ship.angle = ship.angle + (10*ship.direction)
        ship.angle = transformAngleTo360(ship.angle)

    if ship.is_forward or ship.speed > 0:
        ship.postX = (ship.postX + math.cos(math.radians(ship.angle))*ship.speed)
        ship.postY = (ship.postY + -math.sin(math.radians(ship.angle))*ship.speed)
        
        if ship.is_forward == False:
            ship.speed -= 0.2

def isCollision(objectAx, objectAy, objectBx, objectBy, _range):
    distance = math.sqrt(math.pow(objectAx - objectBx, 2) + math.pow(objectAy - objectBy, 2))

    if distance < _range:
        return True
    else:
        return False

def isCollitionWithBullet(objectAx, objectAy, _range):
    global bullet_number
    _isCollision = False

    if bullet_number > 0:
        for i in range(0, bullet_number):
            _isCollision = isCollision(objectAx, objectAy, bullets[i].postX, bullets[i].postY, _range)

    return _isCollision

def isCollitionWithBullet2(objectAx, objectAy):
    global bullet_number
    _isCollision = False

    if bullet_number > 0:
        for i in range(0, bullet_number):
            _isCollision = collider.RectangleCollision(objectAx-40, objectAy-40, clAsteroid.width, clAsteroid.height, 
                    bullets[i].postX-10, bullets[i].postY-10, clBullet.width, clBullet.height)
            #isCollision(objectAx, objectAy, bullets[i].postX, bullets[i].postY, _range)

    return _isCollision

def update_screen():
    pygame.display.update()
    #fps.tick(60)
    configurations.gameFPSClock.tick(configurations.GAME_FPS)            

#init call functions
init_game_data()
draw_init(screen)

#calculations
def game_logic():
    global running, pressedKey
    global bullet_angle, bullet_number, bullet_x, bullet_y
    global ship_x, ship_y

    #move of bullet
    for i in range(0, bullet_number):        
        bullets[i].postX = (bullets[i].postX + math.cos(math.radians(bullets[i].angle))*bullet_speed)
        bullets[i].postY = (bullets[i].postY + -math.sin(math.radians(bullets[i].angle))*bullet_speed)
        if pressedKey:
            print('bullet_y: ' + str(bullets[i].postY) + " - angle: " + str(bullets[i].angle))
            pressedKey = False

    #position asteroids and calculation limit of the screen
    for i in range(0, asteroid_amount):
        #if(isCollitionWithBullet(asteroid[i].postX, asteroid[i].postY, 30) == False):
        if(isCollitionWithBullet2(asteroid[i].postX, asteroid[i].postY) == False):
            asteroid[i].postX = (asteroid[i].postX + math.cos(math.radians(asteroid[i].angle))*asteroid[i].speed)
            asteroid[i].postY = (asteroid[i].postY + -math.sin(math.radians(asteroid[i].angle))*asteroid[i].speed)

            if asteroid[i].postX > configurations.screenWidth + 10:
                asteroid[i].postX = 0
            elif asteroid[i].postX < -10:
                asteroid[i].postX = configurations.screenWidth

            if asteroid[i].postY > configurations.screenHeight + 10:
                asteroid[i].postY = 0
            elif asteroid[i].postY < - 10:
                asteroid[i].postY = configurations.screenHeight
        else:
            asteroid[i].postX = -0
            asteroid[i].postY = -0

        #collision player and asteroid
        if isCollision(ship.postX, ship.postY, asteroid[i].postX, asteroid[i].postY, 27):
            print('Game over')
            running = False

    #position player calculation limit of screen
    if ship.postX > configurations.screenWidth - 50:
        ship.postX = configurations.screenWidth - 50
    elif ship.postX < -50:
        ship.postX = -50

    if ship.postY > configurations.screenHeight - 50:
        ship.postY = configurations.screenHeight - 50
    elif ship.postY < -50:
        ship.postY = -50

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()

