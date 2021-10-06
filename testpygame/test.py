import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pruebas')

running = True

def handle_input():
    global running
    print('handle_input')
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            print('event QUIT')
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

while running:
    handle_input()