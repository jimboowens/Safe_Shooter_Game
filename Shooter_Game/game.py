# 1.Include pygame
import pygame

# 2.Init pygame
#--in order to use pygame we have to run the init method
pygame.init()

# 3.Create a screen with a size
#--the screen size must be a tuple
screen_size = (512,480)

#tell pygame to set the screen up and store it so pygame can use it
pygame_screen = pygame.display.set_mode(screen_size)

#set the title of the window
pygame.display.set_caption("Goblin Chase")

#VARIABLES FOR OUR GAME
background_image = pygame.image.load("layer_one.png")
hero_image = pygame.image.load("hero.png")
goblin_image = pygame.image.load("goblin.png")
monster_image = pygame.image.load("monster.png")


# 4.Create the game loop (while 1)
#create a boolean for whether game should run or not
game_on = True
while game_on:
    #we are inside the main game loop
    #it will keep running as long as our boolean is true

    # 5.Add a quit event (requires sys)
    #pygame comes with an event loop (like JS)
    for event in pygame.event.get():
        
        #we need to give pygame a way out. 
        #if we dont python will freak out
        #because it's inside of an infinity loop
        if(event.type == pygame.QUIT):
            game_on = False

# 6.Screen.fill (pass bg_color)
#we want to draw on the screen
#we are going to use blit (block image transfer)
#blit is a function and takes two arguments:
#--1. what do you want to draw?
#--2. where do you want to draw?
    pygame_screen.blit(background_image,[0,0])

# 7.Flip the screen and start ove4
    pygame.display.flip()

