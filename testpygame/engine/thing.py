import engine.collider as col

class Thing:
    def __init__(self, name):
        self.angle = 0
        self.changeX = 0
        self.changeY = 0
        self.collider = None
        self.directionX = 1
        self.directionY = -1
        self.image = None
        self.isInterfere = False
        self.isMoving = False
        self.name = name
        self.postX = 0
        self.postY = 0
        self.speed = 0
        self.type = 1 #[1 - player, 2 - Obstacle, etc]

    def SetRectCollider(self, width, height):
        self.collider = col.Rectangle(width, height)
        
