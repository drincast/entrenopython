import configurations as config

#constants
INI_POST_Y = config.screenHeight-120

def initThingPlayer(player):    
    player.changeX = player.postX
    player.isMoving = False
    player.munition = 3
    player.isShooting = False
    player.isJump = False
    player.incrementJump = 6
    player.limitJump = 90

def initBullet(bullet):
    bullet.decreseSpeed = 0
    bullet.SetRectCollider(0, bullet.width - 1, bullet.height - 1)

def initMoveBullet(bullet, x, y, direction):
    bullet.postX = x+(bullet.speed*direction)
    bullet.postY = y+10
    bullet.speed = 20
    bullet.decreseSpeed = 0
    bullet.directionX = direction
    bullet.isMoving = True

def initThingObstacle(thing, x, y):
    thing.type = 2
    dummy.postY = y
    dummy.postx = x

def initThingSurfaceV(thing, direction):
    thing.SetLineCollider(1, direction, thing.postX, thing.postY, thing.width, thing.height)