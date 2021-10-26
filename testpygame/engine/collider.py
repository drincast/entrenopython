class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

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

def RectangleCollisionThing(thing1, thing2):
    collision = False

    if(thing1.postX >= thing2.postX and thing1.postX <= thing2.postX+thing2.collider.width 
        and thing1.postY >= thing2.postY and thing1.postY <= thing2.postY+thing2.collider.height):
        collision = True
    elif(thing1.postX+thing1.collider.width >= thing2.postX and thing1.postX+thing1.collider.width <= thing2.postX+thing2.collider.width 
        and thing1.postY+thing1.collider.height >= thing2.postY and thing1.postY+thing1.collider.height <= thing2.postY+thing2.collider.height):
        collision = True

    return collision