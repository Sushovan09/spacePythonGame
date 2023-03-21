import pygame
import random

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#title and icon 
pygame.display.set_caption(" Space Inveders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)



#player
playerImg = pygame.image.load('spaceshipMain.png')
playerX = 370
playerY = 480

#enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,736)
enemyY = random.randint(0,150)

enemyX_change = 0
enemyY_change = 0

#enemy element movement
enemyX_change = .3


#the ammount of x is changing each itaration of the while loop
changeX = 0



def player():
    screen.blit(playerImg,(playerX,playerY))

def enemy():
    screen.blit(enemyImg,(enemyX,enemyY))

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        #if keystroke is pressend check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #print("left arrow is pressed") 
                changeX =  -.3
            if event.key == pygame.K_RIGHT:
                #print("right arrow is pressed") 
                changeX =  +.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("keystroke has been released")
                changeX =  0




    #defining boundary for the enemy
    if(enemyX < 0):
        enemyX = 0
        enemyX_change = +.3
        enemyY_change = +40
    #defining boundary for the enemy
    elif(enemyX > 736):
        enemyX = 736
        enemyX_change = -.3
        enemyY_change = +40
    else:
        enemyY_change = 0

    #real movement for the enemy
    enemyX += enemyX_change
    enemyY += enemyY_change





    #defining boundary for the spaceship
    if(playerX < 0):
        playerX = 0
    #defining boundary for the spaceship
    elif(playerX > 736):
        playerX = 736
    # actually changing the x quardinate of the element 
    else:
        playerX += changeX

    #RGB - Red, Green ,Blue
    screen.fill((0,0,0))
    


    player()
    enemy()
    pygame.display.update()


