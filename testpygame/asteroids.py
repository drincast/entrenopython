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

#variables for player
ship_x = configurations.screenWidth/2 - 50
ship_y = configurations.screenHeight/2 - 50
ship_angle = 0
ship_is_rotating = False
ship_direction = -1

#functions
# functions load init
def draw_init(canvas):
    canvas.fill(BLACK)
    
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
    global bg, debris, ship, time
    posx = time*.3    
    canvas.blit(bg, (0,0))
    canvas.blit(debris, (posx,0))
    canvas.blit(debris, (posx-configurations.screenWidth, 0))
    time = time + 1
    #canvas.blit(rot_center(ship, time), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    canvas.blit(rot_center(ship, ship_angle), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    
# handle inputs function
def handle_input():
    global running, ship_angle, ship_direction, ship_is_rotating

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
        elif event.type == pygame.KEYUP:
            ship_is_rotating = False
            
    if ship_is_rotating:
        ship_angle = ship_angle + (10*ship_direction)

def update_screen():
    pygame.display.update()
    #fps.tick(60)
    configurations.gameFPSClock.tick(configurations.GAME_FPS)            

#init call functions
draw_init(screen)

#game loop
while running:
    draw(screen)
    handle_input()
    #game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()

