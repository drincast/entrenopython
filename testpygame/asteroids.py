import math, os, random, sys
import pygame

#imports me
import configurations

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

#load images
bg = pygame.image.load(configurations.PATH_RES_IMG + '/asteroids/bg.jpg')
debris = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'debris2_brown.png'))
ship = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'ship.png'))
ship_thrusted = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'ship_thrusted.png'))
asteroid = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'asteroid.png'))
bullet = pygame.image.load(os.path.join(configurations.PATH_RES_IMG, 'asteroids', 'shot2.png'))

#variables for player
ship_x = configurations.screenWidth/2 - 50
ship_y = configurations.screenHeight/2 - 50
ship_angle = 0
ship_is_rotating = False
ship_direction = -1
ship_is_forward = False
ship_speed = 0

#variables for asteroids
asteroid_x = []
asteroid_y = []
asteroid_angle = []
asteroid_amount = random.randint(0, 20)
asteroid_speed = 2

#variables for bullet
# bullet_x = 0
# bullet_y = 0
# bullet_angle = 0
bullet_x = []
bullet_y = []
bullet_angle = []
bullet_speed = 5
bullet_number = 0

#varibles of tested
pressedKey = False

#functions
# functions load init
def init_game_data():
    global asteroid_amount
    #asteroids random position 
    for i in range(0, asteroid_amount):
        asteroid_x.append(random.randint(0, configurations.screenWidth))
        asteroid_y.append(random.randint(0, configurations.screenHeight))
        asteroid_angle.append(random.randint(0, 365))
        
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
    global asteroid, asteroid_amount, asteroid_x, asteroid_y
    global bullet_number
    global ship, ship_angle, ship_is_forward, ship_x, ship_y
    posx = time*.3    
    canvas.blit(bg, (0,0))
    canvas.blit(debris, (posx,0))
    canvas.blit(debris, (posx-configurations.screenWidth, 0))

    for i in range(0,asteroid_amount):
        canvas.blit(rot_center(asteroid,time), (asteroid_x[i], asteroid_y[i]))    
    
    time = time + 1
    #canvas.blit(rot_center(ship, time), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    #canvas.blit(rot_center(ship, ship_angle), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    canvas.blit(rot_center(ship, ship_angle), (ship_x, ship_y))

    if (posx-configurations.screenWidth) >= 1:
        print("time: " + str(time) + " - posx: " + str(posx) + " - width: " + str(configurations.screenWidth))
        #running = False
        time = 0

    if ship_is_forward:
        canvas.blit(rot_center(ship_thrusted, ship_angle), (ship_x, ship_y))
    else:
        canvas.blit(rot_center(ship, ship_angle), (ship_x, ship_y))

    for i in range(0, bullet_number):
        #canvas.blit(bullet, (bullet_x,bullet_y))
        canvas.blit(bullet, (bullet_x[i],bullet_y[i]))
    
# handle inputs function
def handle_input():
    global running, ship_angle, ship_direction, ship_is_forward, ship_is_rotating, pressedKey
    global bullet_angle, bullet_number, bullet_x, bullet_y
    global ship_x, ship_y, ship_speed

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
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_is_rotating = True
                ship_direction = 1
            elif event.key == pygame.K_RIGHT:
                ship_is_rotating = True
                ship_direction = -1
            elif event.key == pygame.K_UP:
                ship_is_forward = True
                ship_speed = 10
            elif event.key == pygame.K_SPACE:
                bullet_angle.append(ship_angle)
                bullet_x.append(ship_x + 45 + (25 * transforAngle_0To1_forX(bullet_angle[len(bullet_angle)-1])))
                bullet_y.append(ship_y + 45 + (25 * transforAngle_0To1_forY(bullet_angle[len(bullet_angle)-1])))
                # bullet_y = ship_y + 45 + (-20 * if ship_angle < 181 else 20)                
                bullet_number += 1
                pressedKey = True
        elif event.type == pygame.KEYUP:
            ship_is_rotating = False
            ship_is_forward = False
            
    if ship_is_rotating:
        ship_angle = ship_angle + (10*ship_direction)
        ship_angle = transformAngleTo360(ship_angle)

    if ship_is_forward or ship_speed > 0:
        ship_x = (ship_x + math.cos(math.radians(ship_angle))*ship_speed)
        ship_y = (ship_y + -math.sin(math.radians(ship_angle))*ship_speed)
        
        if ship_is_forward == False:
            ship_speed -= 0.2

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
            _isCollision = isCollision(objectAx, objectAy, bullet_x[i], bullet_y[i], _range)

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
        bullet_x[i] = (bullet_x[i] + math.cos(math.radians(bullet_angle[i]))*bullet_speed)
        bullet_y [i] = (bullet_y[i] + -math.sin(math.radians(bullet_angle[i]))*bullet_speed)
        if pressedKey:
            print('bullet_y: ' + str(bullet_y[i]) + " - angle: " + str(bullet_angle[i]))
            pressedKey = False

    #position asteroids and calculation limit of the screen
    for i in range(0, asteroid_amount):
        if(isCollitionWithBullet(asteroid_x[i], asteroid_y[i], 20) == False):
            asteroid_x[i] = (asteroid_x[i] + math.cos(math.radians(asteroid_angle[i]))*asteroid_speed)
            asteroid_y[i] = (asteroid_y[i] + -math.sin(math.radians(asteroid_angle[i]))*asteroid_speed)

            if asteroid_x[i] > configurations.screenWidth + 10:
                asteroid_x[i] = 0
            elif asteroid_x[i] < -10:
                asteroid_x[i] = configurations.screenWidth

            if asteroid_y[i] > configurations.screenHeight + 10:
                asteroid_y[i] = 0
            elif asteroid_y[i] < - 10:
                asteroid_y[i] = configurations.screenHeight
        else:
            asteroid_x[i] = -0
            asteroid_y[i] = -0

        #collision player and asteroid
        if isCollision(ship_x, ship_y, asteroid_x[i], asteroid_y[i], 27):
            print('Game over')
            running = False

    #position player calculation limit of screen
    if ship_x > configurations.screenWidth - 50:
        ship_x = configurations.screenWidth - 50
    elif ship_x < -50:
        ship_x = -50

    if ship_y > configurations.screenHeight - 50:
        ship_y = configurations.screenHeight - 50
    elif ship_y < -50:
        ship_y = -50

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()

