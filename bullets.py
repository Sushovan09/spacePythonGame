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

#background
background = pygame.image.load("background.png")

#player
playerImg = pygame.image.load('spaceshipMain.png')
playerX = 370
playerY = 480

#the ammount of x is changing each itaration of the while loop
changeX = 0

#enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,736)
enemyY = random.randint(0,150)

enemyX_change = 0
enemyY_change = 0

#enemy element movement
enemyX_change = 4


#bullets

bulletsImg = pygame.image.load('missile.png')
bulletsX = playerX
bulletsY = 480

bulletsY_change = -3
#ready - you can't see the bullets on the screen 
#fire the bullets is currently moving 
bullets_state = 'ready'


def player():
    screen.blit(playerImg,(playerX,playerY))

def enemy():
    screen.blit(enemyImg,(enemyX,enemyY))

#def bullets():
#    screen.blit(bulletsImg,(bulletsX,bulletsY))

def fire_bullet(x,y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bulletsImg,(x,y))


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
                changeX =  -5
            if event.key == pygame.K_RIGHT:
                #print("right arrow is pressed") 
                changeX =  +5
            if event.key == pygame.K_SPACE:
                #print("space bar is pressed")
                fire_bullet(playerX,bulletsY)
                bulletsX = playerX +16
                bulletsY = 480
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print("keystroke has been released")
                changeX =  0




    #defining boundary for the enemy
    if(enemyX < 0):
        enemyX = 0
        enemyX_change = +4
        enemyY_change = +40
    #defining boundary for the enemy
    elif(enemyX > 736):
        enemyX = 736
        enemyX_change = -4
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
    #background image
    screen.blit(background,(-200,-60))
    
    # movement for bullets every visible component will have to be  after      
    # screen.fill((0,0,0))     screen.blit(background,(-200,-60) 
    # component otherwise we will not able to see it

    if bullets_state =="fire":
        fire_bullet(bulletsX,bulletsY)
        print(bulletsX,bulletsY)
        bulletsY += bulletsY_change

    player()
    enemy()
    
    pygame.display.update()


