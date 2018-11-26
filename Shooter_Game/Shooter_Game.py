# 1. we needed pip to get this for us because python doesn't ship with it
import pygame
from Hero import Hero
from Bad_guy import Bad_guy
from Weapon import Arrow
# from Weapon import Weapon
# 2. initiate pygame
pygame.init()
hero = Hero()
bad_guy = Bad_guy()
arrow = Arrow(hero, bad_guy)
# 3. make a screen with a size
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# 4. set the title of the game
pygame.display.set_caption('Robin Hood')
#===========VARIABLES FOR OUR GAME===========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')

# ===========MAIN GAME LOOP===========
game_on = True
while game_on:
    #  we are in the game loop from here on out
    # 5. Listen for the user to click the red x
    for event in pygame.event.get():
        # print (event.key)  
        if event.type == pygame.QUIT:
            # the user chose to exit
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 273:
                # hero.y -= 8
                hero.should_move('up')
            elif event.key == 274:
                # hero.y += 8
                hero.should_move('down')
            if event.key == 275:
                # hero.x += 8 
                hero.should_move('left')
            elif event.key == 276:
                # hero.x -= 8
                hero.should_move('right')
            elif event.key == 32:
                arrow.fire(arrow, bad_guy)
        elif event.type == pygame.KEYUP:
            if event.key == 273:
                # hero.y -= 8
                hero.should_move('up', False)
            elif event.key == 274:
                # hero.y += 8
                hero.should_move('down', False)
            if event.key == 275:
                hero.x += 8 
                hero.should_move('left', False)
            elif event.key == 276:
                hero.x -= 8
                hero.should_move('right', False)
    # ===========DRAW STUFF===========
    # we use blit to draw on the screen, blit  = block image transfer
    # it takes two arguments - 
        # 1. what to draw
        # 2. where to draw it
    # in the docs, SURFACE = our 'pygame.screem'
    pygame_screen.blit(background_image,[0,0])
    hero.draw_me()
    pygame_screen.blit(hero_image,[hero.x,hero.y])
    bad_guy.update_me(hero)
    pygame_screen.blit(monster_image, [bad_guy.x,bad_guy.y])
    pygame_screen.blit(arrow_image,[arrow.x,arrow.y])
    pygame.display.flip() #this is to flip to the next "slide".. it deleted the former one and replaces it
    print (bad_guy.health)
