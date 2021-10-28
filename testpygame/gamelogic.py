import configurations as config

import engine.collider as collider
import initThingGame as initTG

def GameLogic(bullets, time, dummys, player):
    # player.changeX = player.postX
    if(player.isMoving):
        player.postX += player.speed*player.direction

    if(player.isJump):
        player.postY += 5*(player.directionY) #up decrement position in y, -1 is for direction is up
        if player.postY <= ((initTG.INI_POST_Y - player.limitJump) + 10):
            player.directionY = 1
        elif player.postY >= initTG.INI_POST_Y:
            player.postY = initTG.INI_POST_Y
            player.isJump = False
            player.directionY = -1

    #collider section
    for i in range(0,len(dummys)):
        # _isCollision = collider.RectangleCollision(player.postX+5, player.postY+5, 20, 50, 
        #             dummys[i].postX+5, dummys[i].postY+5, 20, 50)
        
        _isCollision = collider.RectangleCollisionThing(player, dummys[i])
        #si es en especifico, seria identificar dentro del ciclo la colisión
        if _isCollision:            
            print('collisión ----')
            if(dummys[i].type == 2):
                player.isInterfere = True

        for item in bullets:
            # _isCollision = collider.RectangleCollision(dummys[i].postX+5, dummys[i].postY+5, 20, 50, 
            #         item.postX+1, item.postY+1, 19, 9)
            _isCollision = collider.RectangleCollisionThing(item, dummys[i])
            # _isCollision = collider.RectangleCollisionThing(dummys[i], item)
            if _isCollision:
                print('colision with bullet ----')
                print('bullet: ', item.name, item.postX, item.postY, item.collider.width, item.collider.height
                    , dummys[i].postX, dummys[i].postY, dummys[i].collider.width, dummys[i].collider.height)

    for item in bullets:
        if(item.isMoving):
            item.postX = item.postX + (item.direction*(item.speed - item.decreseSpeed))
            if(time%3 == 0):
                item.decreseSpeed = (item.decreseSpeed + 1, 15)[item.decreseSpeed >= 15]
            # print(time, time%3)
        
        if(player.isShooting and not item.isMoving):        
            #for item in bullets:
            print(item.name, item.isMoving, item.postX)
            if(item.postX == -100):
                initTG.initMoveBullet(item, player.postX, player.postY, player.direction)
                item.isMoving = True            
                player.isShooting = False #the player already shoot

        if(config.screenWidth + 5 < item.postX or -5 > item.postX):
            if(item.postX != -100):
                print(item.name)
            item.postX = -100
            item.isMoving = False        

        # if(len(bullets) <= 0):
        #     bullets.append(engine.Thing("bullet01"))
        # else:
        #     if(len(bullets) <= 3):
        #         bullets.append(engine.Thing("bullet0" + str(len(bullets)-1)))
        #     else:
        #         for item in bullets:
        #             if(item.postX == -100):
        #                 initTG.initBullet(item, player.postX, player.postY, player.direction)
        #                 item.isMoving = True

    #recorrido de bullets para movimiento de bullets

    # if(not player.isInterfere):
    #     player.postX = player.changeX