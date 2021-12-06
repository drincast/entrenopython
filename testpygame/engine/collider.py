class Rectangle:
    def __init__(self, vadd, w, h):
        self.height = h
        self.valueAdd = vadd
        self.width = w

class SolidSurface:
    def __init__(self, type, direction, dimensions):
        #line - 0 horizontal, 1 vertical
        #dimensions - (postX, postY, width, height)
        self.type = type
        self.direction = direction  #-1 left, up, 1 right, down
        self.dimensions = dimensions        

def RectangleCollision(rx1, ry1, w1, h1, rx2, ry2, w2, h2):
    collision = False
    
    # if(rx1 > rx2+w2):
    #     if(rx1+w1 < rx2):
    #         if(ry1 > rx2+h2):
    #             if(ry1+h1 < rx2):
    #                 collision = False

    if(rx1 >= rx2 and rx1 <= rx2+w2 and ry1 >= ry2 and ry1 <= ry2+h2):
        collision = True
    elif(rx1+w1 >= rx2 and rx1+w1 <= rx2+w2 and ry1+h1 >= ry2 and ry1+h2 <= ry2+h2):
        collision = True

    return collision

#the firts thing is smaller
def RectangleCollisionThing(thing1, thing2):
    collision = False
    x1 = thing1.postX + thing1.collider.valueAdd
    y1 = thing1.postY + thing1.collider.valueAdd
    x2 = thing2.postX + thing2.collider.valueAdd
    y2 = thing2.postY + thing2.collider.valueAdd

    if(x1 >= x2 and x1 <= x2+thing2.collider.width 
        and y1 >= y2 and y1 <= y2+thing2.collider.height):
        collision = True
        print("uno")
    elif(x1+thing1.collider.width >= x2 and x1+thing1.collider.width <= x2+thing2.collider.width 
        and y1+thing1.collider.height >= y2 and y1+thing1.collider.height <= y2+thing2.collider.height):
        collision = True
        print("dos")

    return collision

# def SurfaceCollider(solidSurface, x, size):
#     collision = False

#     if(solidSurface.type == 0):
#         collision = False
#     else:
#         if(solidSurface.collider.direction == 1): # right
#             if(x + size >= solidSurface.collider.dimensions[0]):
#                 collision = True
#         else:
#             if(x <= solidSurface.collider.dimensions[0]):
#                 collision = True
#     return collision

def SurfaceCollider(solidSurface, thing):
    collisionX = False
    collisionY = False
    directionX = -1
    directionY = -1

    surfaceWidth = solidSurface.postX + solidSurface.width
    thingWidth = thing.changeX + thing.width

    surfaceHeight = solidSurface.postY + solidSurface.height
    thingHeight = thing.changeY + thing.height

    if(thing.changeX >= solidSurface.postX and thing.changeX <= surfaceWidth):
        collisionX = True        
    elif(thingWidth >= solidSurface.postX and thingWidth <= surfaceWidth):
        directionX = 1
        collisionX = True

    if(thing.postY >= solidSurface.postY and thing.postY <= surfaceHeight):
        collisionY = True        
    elif(thingHeight >= solidSurface.postY and thingHeight <= surfaceHeight):
        directionY = 1
        collisionY = True
    
    #print([[collisionX, collisionY], [directionX, directionY]]) 
    return [[collisionX, collisionY], [directionX, directionY]]


def ThingInSurfaceRangeY(thingY, thingHeight, surfaceY, surfaceHeight):
    collisionY = False
    
    if((thingY >= surfaceY and thingY <= surfaceHeight)
        or thingHeight >= surfaceY and thingHeight <= surfaceHeight):
        collisionY = True
    
    return collisionY

# def SurfaceCollider2(solidSurface, thing):
#     #([collX, collY], [collRight, collLeft], [collDown, collUp])
#     collisionSurface = [[0,0], [0,0], [0,0]]
#     surfaceWidth = solidSurface.postX + solidSurface.width
#     thingWidth = thing.postX + thing.width
#     surfaceHeight = solidSurface.postY + solidSurface.height
#     thingHeight = thing.changeY + thing.height

#     #coliciona visualmente en el lado de arriba del bloque o figura
#     collisionSurface[0][1] = (thing.postY + (thing.height/2) <= solidSurface.postY)

#     #la parte inferior toco la superior
#     if(collisionSurface[0][1]):
#         #if (thing.changeX >= solidSurface.postX and thing.changeX <= surfaceWidth):
#         if (thing.postX >= solidSurface.postX and thing.postX <= surfaceWidth):
#             #and ThingInSurfaceRangeY(thing.postY, thingHeight, solidSurface.postY, surfaceHeight)):        
#             print('collisionYPrevious', collisionSurface[1])
#             print("choco thing a su izquierda -->")
#             print("a nivel de thing.postX", thing.postX)
#             collisionSurface[0][0] = True
#             collisionSurface[1][1] = True
#         elif (thingWidth >= solidSurface.postX and thingWidth <= surfaceWidth):
#             print("a nivel de thingWidth", thingWidth)
#             collisionSurface[0][0] = True
#             collisionSurface[1][1] = True
#     else:
#         if (thing.postX >= solidSurface.postX and thing.postX <= surfaceWidth):
#             print('thing colisionó a su izquierda', thing.postX)
#             collisionSurface[0][0] = True
#             collisionSurface[1][1] = True
#         elif (thingWidth >= solidSurface.postX and thingWidth <= surfaceWidth):
#             print('thing colicionó a su derecha', thingWidth)
#             collisionSurface[0][0] = True
#             collisionSurface[1][0] = True

#     # return [[collisionX, collisionY], [directionX, directionY]]
#     return collisionSurface

def ColliderSurfaceForUp(solidSurface, thing):
    #([collX, collY], [collRight, collLeft], [collDown, collUp])
    collisionSurface = [[0,0], [0,0], [0,0]]
    surfaceWidth = solidSurface.postX + solidSurface.width
    thingWidth = thing.postX + thing.width
    surfaceHeight = solidSurface.postY + solidSurface.height
    thingHeight = thing.changeY + thing.height

    #colisiona visualmente en el lado de arriba del bloque o figura
    collisionSurface[0][1] = (thing.postY + (thing.height/2) <= solidSurface.postY)

    if (thing.postX >= solidSurface.postX and thing.postX <= surfaceWidth):
        #and ThingInSurfaceRangeY(thing.postY, thingHeight, solidSurface.postY, surfaceHeight)):        
        print('collisionYPrevious', collisionSurface[1])
        print("choco thing a su izquierda -->")
        print("a nivel de thing.postX", thing.postX)
        collisionSurface[0][0] = True
        collisionSurface[1][1] = True
    elif (thingWidth >= solidSurface.postX and thingWidth <= surfaceWidth):
        print("a nivel de thingWidth", thingWidth)
        collisionSurface[0][0] = True
        collisionSurface[1][0] = True

    return collisionSurface

#TODO: mejorar el nombre de la función
#this fuction is for dectect of collision with square and, the object thing
#change of position on the top of surface
def PNCollisionSquareSurfaceBelow(resCollision, thing, surface):
    if(resCollision[0][0] and resCollision[0][1]):
        thing.changeY = surface.postY - thing.height - 1
        thing.iniPostY = thing.changeY
    elif(resCollision[0][0] and not resCollision[0][1]):
        if(resCollision[1][0]):
            thing.changeX = surface.postX - surface.width - 1
        elif(resCollision[1][1]):
            thing.changeX = surface.postX + surface.width + 1
