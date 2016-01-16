'''Auther            : HeFengChen
   Date last modified: Apr 24 2011
   Description       : The program simulates a game of sea warfare. The player controls
                       the movement of a destoryer. There will be multiple submarines coming
                       over under the sea. The player can attack the submarines by dropping
                       depth charges on them. The submarines can attack the player uing water
                       mines and missles. The player needs to destory as many submarines as
                       possible to earn high scores. The score will be store in a file called
                       hall of fame. The player can view the top ten scores in the Hall of 
                       Fame option. Enjoy.'''


# I - IMPORT AND INITIALIZE 
import pygame, gameSprite,random,game_functions
pygame.init() 
screen = pygame.display.set_mode((640, 480)) 

joysticks = [] 
for joystick_no in range(pygame.joystick.get_count()): 
    stick = pygame.joystick.Joystick(joystick_no) 
    stick.init() 
    joysticks.append(stick) 
      

def main():
    
    # D - DISPLAY 
    pygame.display.set_caption("menu") 
    
    background = pygame.image.load("Picture/menu_background.png")
    screen.blit(background, (0, 0))
    
    # Sprites for: three labels lead to three different options and cursor
    label_1 = gameSprite.Label('Play',(320,150))
    label_2 = gameSprite.Label('Hall of Fame', (320,250))
    label_3 = gameSprite.Label('Exit',(320,350))
    cursor = gameSprite.Cursor()
    
    allSprites = pygame.sprite.OrderedUpdates(label_1,label_2,label_3,cursor)
    
    # A - ACTION:
    
    # A -- ASSIGN 
    clock = pygame.time.Clock() 
    keepGoing = True
    
    # Hide the mouse pointer 
    pygame.mouse.set_visible(False)
    
    # L -- LOOP 
    while keepGoing: 
      
        # T -- TIME 
        clock.tick(30) 
      
        # E -- EVENT HANDLING: Player1 uses arrow keys, Player2 uses joystick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            
            # if a mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()
                
                # check if the cursor is on the first option
                if (mouse_xy[0] < label_1.rect.right) and (mouse_xy[0] > label_1.rect.left) and (mouse_xy[1] < label_1.rect.bottom) and (mouse_xy[1] > label_1.rect.top):
                    # if true, call the game function to start game
                    game_functions.game()
                    # when game finishes, return to the menu background
                    screen.blit(background, (0, 0))
                    
                # check if the cursor is on the second option    
                elif mouse_xy[0] < label_2.rect.right and mouse_xy[0] > label_2.rect.left and mouse_xy[1] < label_2.rect.bottom and mouse_xy[1] > label_2.rect.top:
                    # if true, call the hall of fame displaying function to display hall of fame
                    game_functions.fame_display()
                    
                # check if the cursor is on the third option
                elif mouse_xy[0] < label_3.rect.right and mouse_xy[0] > label_3.rect.left and mouse_xy[1] < label_3.rect.bottom and mouse_xy[1] > label_3.rect.top:
                    # if true, quit the game
                    keepGoing = False
                    
        # check if the cursor collides with any labels. if so, change their color
        if pygame.sprite.collide_rect(cursor,label_1):
            label_1.color_change()
        elif pygame.sprite.collide_rect(cursor,label_2):
            label_2.color_change()
        elif pygame.sprite.collide_rect(cursor,label_3):
            label_3.color_change()
            
                    
                    
        # R -- REFRESH SCREEN       
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        
        
        pygame.display.flip()
        screen.blit(background, (0, 0))
        
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
        
    # Quit the game
    pygame.quit()

# Call the main function 
main()

