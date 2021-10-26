import engine.collider as col

class Thing:
    def __init__(self, name):
        self.angle = 0
        self.changeX = 0
        self.changeY = 0
        self.image = None
        self.name = name
        self.postX = 0
        self.postY = 0
        self.speed = 0
        self.isMoving = False
        self.collider = None

    def SetRectCollider(width, height):
        coll = col.Rectangle(width, height)
        return coll
