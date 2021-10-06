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
pygame.display.set_caption('Name of Game')


#functions
def init_game_data():
    return False

def draw_init(canvas):
    canvas.fill(BLACK)

def draw(canvas):
    return False

def handle_input():
    return False

def update_screen():
    pygame.display.update()
    configurations.gameFPSClock.tick(configurations.GAME_FPS)

#init call functions
init_game_data()
draw_init(screen)

#calculations
def game_logic():
    return False

#game loop
while running:
    draw(screen)
    handle_input()
    game_logic()
    update_screen()

print(configurations.PATH_RES_IMG)

pygame.quit()
sys.exit()