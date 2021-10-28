import configurations as config

#constants
INI_POST_Y = config.screenHeight-120

def initThingPlayer(player):
    player.postX = config.screenWidth/2 - 50
    player.changeX = player.postX
    player.postY = INI_POST_Y
    player.speed = 5
    player.direction = 1
    player.isMoving = False
    player.munition = 3
    player.isShooting = False
    player.isJump = False
    player.incrementJump = 6
    player.limitJump = 90
    player.directionY = -1

def initThingDummy(dummy, x, y):
    dummy.postX = x
    dummy.postY = y
    dummy.speed = 5
    dummy.direction = 1
    dummy.isMoving = False

def initBullet(bullet):
    bullet.postX = -100
    bullet.postY = -100
    bullet.speed = 20
    bullet.direction = 1
    bullet.decreseSpeed = 0
    bullet.SetRectCollider(0, 19, 9)

def initMoveBullet(bullet, x, y, direction):
    bullet.postX = x+(bullet.speed*direction)
    bullet.postY = y+10
    bullet.speed = 20
    bullet.decreseSpeed = 0
    bullet.direction = direction
    bullet.isMoving = True

def initThingObstacle(thing, x, y):
    thing.type = 2
    dummy.postY = y
    dummy.postx = x

def initThingSurfaceV(thing, direction, x, y, width, height):
    thing.postX = x
    thing.postY = y
    thing.SetLineCollider(1, direction, x, y, width, height)