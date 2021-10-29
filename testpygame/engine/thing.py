import os
import pygame

import configurations as config
import engine.collider as col

class Thing:
    def __init__(self, name):
        self.angle = 0
        self.changeX = 0
        self.changeY = 0
        self.collider = None
        self.directionX = 1
        self.directionY = -1
        self.height = 0
        self.image = None
        self.isInterfere = False #verify for what??
        self.isMoving = False
        self.name = name
        self.postX = 0
        self.postY = 0
        self.speed = 0
        self.type = 1 #[1 - player, 2 - Obstacle, etc]
        self.width = 0

    def initThingBasic(self, x, y, height, width, image, speed, _type=1):
        self.postX = x
        self.postY = y
        self.height = height
        self.width = width
        self.speed = speed
        self.type = _type
        if(isinstance(image, str)):        
            self.image = pygame.image.load(os.path.join(config.PATH_RES_IMG, 'test', image))
        else:
            self.image = image

    def SetRectCollider(self, width, height, vadd):
        self.collider = col.Rectangle(width, height, vadd)

    def SetLineCollider(self, _type, direction, x, y, width, height):
        self.collider = col.SolidSurface(_type, direction, (x, y, width, height))
        
