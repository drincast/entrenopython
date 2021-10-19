import configurations

def initThingPlayer(player):
    player.postX = configurations.screenWidth/2 - 50
    player.postY = configurations.screenHeight-120
    player.speed = 5
    player.direction = 1
    player.isMoving = False

def initThingDummy(dummy, x, y):
    dummy.postX = x
    dummy.postY = y
    dummy.speed = 5
    dummy.direction = 1
    dummy.isMoving = False