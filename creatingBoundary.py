
import pygame

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

#the ammount of x is changing each eteration of the while loop
changeX = 0



def player():
    screen.blit(playerImg,(playerX,playerY))

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
    
    #playerX = playerX - .1
    #playerX = playerX + .1

    #playerY = playerY - .1
    #playerY = playerY - .1



    player()
    pygame.display.update()


