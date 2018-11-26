import pygame
# 2. initiate pygame
pygame.init()
# 3. make a screen with a size
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# 4. set the title of the game
pygame.display.set_caption('Robin Hood')
#===========VARIABLES FOR OUR GAME===========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
arrow_image = pygame.image.load('arrow.png')
herLoc = {
    'x' : 0,
    'y' : 0
}
 # ===========MAIN GAME LOOP===========
game_on = True
while game_on:
    #  we are in the game loop from here on out
    # 5. Listen for the user to click the red x
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            # the user chose to exit
            game_on = False
        elif event.type == pygame.KEYDOWN:
            print (event.key)
            if event.key == 275:
                herLoc['x'] += 10
    # ===========DRAW STUFF===========
    # we use blit to draw on the screen, blit  = block image transfer
    # it takes two arguments - 
        # 1. what to draw
        # 2. where to draw it
    # in the docs, SURFACE = our 'pygame.screem'
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image,[herLoc['x'],herLoc['y']])
    pygame.display.flip() 