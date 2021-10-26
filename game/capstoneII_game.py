# i started the program by compying and pasting the example before making any changes

import pygame
import random

pygame.init()

screen_width =1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# the first change i made was add 2 more enemies and prize by storing them in various variables

player = pygame.image.load("image.png")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg") 
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# i then got width and height of the prize and other 2 enemies as well

image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))


playerXposition = 100
playerYposition = 50

# below i then also made extra enemies and the prize start at random Y positions

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

prizeXPosition =  screen_width
prizeYPosition =  random.randint(0, screen_height - prize_height)

# below to check if the key is pressed down i used boolean values with the left and right key

keyUp=False
keyDown=False
keyLeft=False
keyRight=False

# below i then drawed the other 2 enemies and prize to the screen at the position specified within the while loop


while 1:

    screen.fill(0)
    screen.blit(player, (playerXposition, playerYposition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
# in order to use right and left keys we used the player x postion
# as well as checking whether the selected key is up and not pressed

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                keyUp = True

            if event.key == pygame.K_DOWN:
                keyDown = True
                
            if event.key == pygame.K_RIGHT:
                keyRight = True

            if event.key == pygame.K_LEFT:
                keyLeft = True
                

# i tested to check if the key is released on both righ and left

        if event.type == pygame.KEYUP:
        
            
            if event.key == pygame.K_UP:
                keyUp = False

            if event.key == pygame.K_DOWN:
                keyDown = False

            if event.key == pygame.K_RIGHT:
                keyRight = False

            if event.key == pygame.K_LEFT:
                keyLeft = False

# i used the x position of the the player to move left and right while not leaving game screen window


    if keyUp == True:
        if playerYposition > 0 : 
            playerYposition -= 1
    if keyDown == True:
        if playerYposition < screen_height - image_height:
            playerYposition += 1
    if keyLeft == True:
        if playerXposition > 0:
            playerXposition -=1

    if keyRight == True:
        if playerXposition < screen_width - image_width:
            playerXposition +=1
            

    playerBox = pygame.Rect(player.get_rect())            
    playerBox.top = playerYposition
    playerBox.left = playerXposition

# i then created bounding boxes for the added enemies as well as the prize

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # below if the playerbox collides with any of the 3 enemies you lose   


    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):
        print("You lose!")
        
        pygame.quit()
        exit(0)
        

    # below if the player box collides with the prize box you win
    
    if playerBox.colliderect(prizeBox) :
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player.
    # below i made enemies and the prize approach at different speeds 
    
    enemy1XPosition -= 0.10
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.25
    prizeXPosition -= 0.08
    
    # ================The game loop logic ends here. =============
  







