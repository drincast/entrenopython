import configurations

def initThingPlayer(player):
    player.postX = configurations.screenWidth/2 - 50
    player.postY = configurations.screenHeight-120
    player.speed = 5
    player.direction = 1
    player.isMoving = False
    player.munition = 3
    player.isShooting = False

def initThingDummy(dummy, x, y):
    dummy.postX = x
    dummy.postY = y
    dummy.speed = 5
    dummy.direction = 1
    dummy.isMoving = False

def initBullet(bullet):
    bullet.postX = -100
    bullet.postY = -100
    bullet.speed = 5
    bullet.direction = 1

def initMoveBullet(bullet, x, y, direction):
    bullet.postX = x+(bullet.speed*direction)
    bullet.postY = y+10
    bullet.speed = 5
    bullet.direction = direction
    bullet.isMoving = True
