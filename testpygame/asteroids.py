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

#functions
# functions load init
def draw_init(canvas):
    canvas.fill(BLACK)
    
#rotate de ship
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#draw game functions
def draw(canvas):
    global bg, debris, time
    posx = time*.3
    canvas.blit(bg, (0,0))
    canvas.blit(debris, (posx,0))
    canvas.blit(debris, (posx-configurations.screenWidth, 0))
    time = time + 1
    canvas.blit(rot_center(ship, time), (configurations.screenWidth/2 - 50, configurations.screenHeight/2 - 50))
    
# handle inputs function
def handle_input():
    global running
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
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

