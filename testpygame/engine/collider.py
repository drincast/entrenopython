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
    elif(x1+thing1.collider.width >= x2 and x1+thing1.collider.width <= x2+thing2.collider.width 
        and y1+thing1.collider.height >= y2 and y1+thing1.collider.height <= y2+thing2.collider.height):
        collision = True

    return collision

def SurfaceCollider(solidSurface, x, size):
    collision = False

    if(solidSurface.type == 0):
        collision = False
    else:
        if(solidSurface.collider.direction == 1): # right
            if(x + size >= solidSurface.collider.dimensions[0]):
                collision = True
        else:
            if(x <= solidSurface.collider.dimensions[0]):
                collision = True
    return collision
