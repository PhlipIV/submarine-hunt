'''Auther            : HeFengChen
   Date last modified: Jun 06 2011
   Description       : The program contains all functions that are needed for
                       the game.'''


# I - IMPORT AND INITIALIZE 
import pygame,gameSprite,random
pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480)) 

        
   
def get_lists():
    '''This function does not take any parameters. It does the first
    stage process of data from the files so that code will be neater.
    This function returns two lists, one contains line number of the
    top ten scores in file_HallOfFame, the other one contains all
    lines in file_HallOfFame.'''
    
    file_HallOfFame = open("Document/HallOfFame.txt","r")
    file_Score = open("Document/Score.txt","r")

    # score_list: list of score in same order as scores in file score
    # top_ten   : list of the top ten scores
    # index_list: list of line number of the top ten scores in file_HallOfFame
    # file_list : list of all lines in file_HallOfFame 
    score_list = []
    top_ten = []
    index_list = []
    file_list = []
    
    # create the top_ten and score_list lists
    for _ in file_Score:
        top_ten.append(int(_))
        score_list.append(int(_))
        top_ten.sort()
        top_ten.reverse()
        top_ten = top_ten[:10]
        
    # find the index of each top ten score in the score_list, append the index to the index_list
    for _ in top_ten:
        index = score_list.index(_)
        index_list.append(index)
    
    # Create the file list
    for _ in file_HallOfFame:
        file_list.append(_)
        
    # close the files
    file_HallOfFame.close()
    file_Score.close()
    
    # return index_list and file_list
    return index_list,file_list





    
def fame_display():
    '''This function takes no parameters. It displays the score and
    name of the ten highest scores. This function does not return
    anything.'''
    
    # D - DISPLAY 
    pygame.display.set_caption("Hall Of Fame") 
      
    # E - ENTITIES 
    background = pygame.image.load("Picture/background2.gif")
    screen.blit(background, (0, 0))
    
    # assign the returned values
    index_list,file_list = get_lists()
    
    # Sprites for: cursor and exit label
    label_1 = gameSprite.Label('Exit',(100,400))
    cursor = gameSprite.Cursor()
    
    fame_list = []
    y_position = 100
    counter = 1
    
    # Create multiple label objects and put them in order
    for element in index_list:
        fame_list.append(gameSprite.Hall_of_fame(str(counter)+". "+file_list[element],(280,y_position)))
        y_position += 20
        counter += 1
        
        
    # Organize all objects by putting them into groups
    allSprites = pygame.sprite.OrderedUpdates(fame_list,label_1,cursor)
    
    # A - ACTION:
    
    # A -- ASSIGN 
    clock = pygame.time.Clock() 
    keepGoing = True
    
    
    # L -- LOOP 
    while keepGoing: 
      
        # T -- TIME 
        clock.tick(30) 
      
        # E -- EVENT HANDLING: mouse control
        for event in pygame.event.get():
             
            
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()
                if mouse_xy[0] < label_1.rect.right and mouse_xy[0] > label_1.rect.left and mouse_xy[1] < label_1.rect.bottom and mouse_xy[1] > label_1.rect.top:
                    keepGoing = False
                    
        # change the label's color if the cursor is on it
        if pygame.sprite.collide_rect(cursor,label_1):
            label_1.color_change()
              
                    
                    
        # R -- REFRESH SCREEN       
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        
        pygame.display.flip()
        
    # Clear everything off the screen
    allSprites.clear(screen, background)
    
    
    
    
    
def game(): 
    '''This function defines the main game logic.'''
       
    # D - DISPLAY 
    pygame.display.set_caption("Game Window") 
      
    # E - ENTITIES 
    background = pygame.image.load("Picture/game_background.jpg")
    screen.blit(background, (0, 0))
   
  
    # Sprites for: Game over sign, player, counter, status bar and Sound Effects 
    label = pygame.font.Font("BURNSTOW.ttf",90)
    game_over = label.render("GAME OVER!",1,(255,0,0))
    
    pygame.mixer.music.load("Sound/music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    depth_charge_launch = pygame.mixer.Sound("Sound/charge.wav")
    depth_charge_launch.set_volume(0.4)
    destory = pygame.mixer.Sound("Sound/destory.wav")
    destory.set_volume(0.4)
    sub_destory = pygame.mixer.Sound("Sound/sub_destory.wav")
    sub_destory.set_volume(0.3)
    explosion = pygame.mixer.Sound("Sound/explode.wav")
    explosion.set_volume(0.4)
    torpedo = pygame.mixer.Sound("Sound/torpedo.wav")
    torpedo.set_volume(0.4)
    mine_sound = pygame.mixer.Sound("Sound/mine1.wav")
    mine_sound.set_volume(0.4)
    
    
    player = gameSprite.Player(screen)
    count = gameSprite.Count()
    status = gameSprite.Status_Bar()
    
    # Create an empty group for each submarine and add submarine objects to it 
    submarines = pygame.sprite.Group()
    mine_submarines = pygame.sprite.Group()
    missle_submarines = pygame.sprite.Group()
    
    for i in range(3):
        submarines.add(gameSprite.Submarine())
        
    for i in range(2):
        mine_submarines.add(gameSprite.Mine_Submarine())
        
    for i in range(2):
        missle_submarines.add(gameSprite.Missle_Submarine())
        
    
    # Create three empty groups for later use
    charges = pygame.sprite.Group()
    mines = pygame.sprite.Group() 
    missles = pygame.sprite.Group() 
    
    # Organize obejcts into groups
    allSprites = pygame.sprite.Group(player,submarines,mine_submarines,missle_submarines,count,status)
    
    # A - ACTION:
    
    # A -- ASSIGN  
    clock = pygame.time.Clock() 
    keepGoing = True
    released = True
    width = 0
    point_check = 0

  
   
  
    # L -- LOOP 
    while keepGoing: 
      
        # T -- TIME 
        clock.tick(30) 
      
        # E -- EVENT HANDLING: Player uses joystick
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: 
                keepGoing = False
                
            if event.type == pygame.JOYHATMOTION:               
                player.change_direction(event.value)
             
            if event.type == pygame.JOYBUTTONDOWN: 
                if status.is_ready():
                    status.reset()
                    charge = gameSprite.Depth_charge(screen,player.rect.centerx)
                    charges.add(charge)
                    depth_charge_launch.play()
           
                    
        # Go through each mine submarine in the group
        for item in mine_submarines:
            
            # Check if the submarine is right below the player
            if (item.rect.centerx < player.rect.centerx+3) and (item.rect.centerx > player.rect.centerx -3) :
                
                # Check if the submarine has released a mine or not
                if item.is_released():
                    
                    # reset the releasing status
                    item.set_released()
                    mine_sound.play()
                    
                    # add the sprite to the group
                    mine = gameSprite.Mine(screen,item.rect.top,item.rect.centerx)
                    mines.add(mine)
        
        # Go through each missle submarine in the group
        for item in missle_submarines:
            
            # Check if the submarine has released a missle or not
            if item.is_released():
                fire_range = item.get_fire_range()
                
                # Check if the submarine has entered its fire range
                if (item.rect.centerx < (fire_range+5)) and (item.rect.centerx > (fire_range - 5)) : 
                    
                    # reset the releasing status
                    item.set_released()
                    torpedo.play()
                    
                     # add the sprite to the group
                    missle = gameSprite.Missle(item.rect.top,item.rect.centerx,player.rect.centerx,player.rect.left,player.rect.right)
                    missles.add(missle)
                    
                
                    
        # Check if the depth charge has collided with a submarine
        for one_charge in charges:
            for one_sub in submarines:
                if one_charge.rect.colliderect(one_sub.rect):
                    destory.play()
                    count.add_score(10)
                    one_sub.set_explode()
                    sub_destory.play()
                    one_charge.kill()
              
        # Check if the depth charge has collided with a mine submarine
        for one_charge in charges:
            for one_sub in mine_submarines:
                if one_charge.rect.colliderect(one_sub.rect):
                    destory.play()
                    count.add_score(20)
                    one_sub.set_explode()
                    sub_destory.play()
                    one_charge.kill()
                    
        # Check if the depth charge has collided with a missle submarine
        for one_charge in charges:
            for one_sub in missle_submarines:
                if one_charge.rect.colliderect(one_sub.rect):
                    destory.play()
                    count.add_score(30)
                    one_sub.set_explode()
                    sub_destory.play()
                    one_charge.kill()
                 
        # Check if the player has collided with a water mine
        mine_collide = pygame.sprite.spritecollide(player, mines, False)
        for one_mine in mine_collide:
            if not one_mine.is_exploded():
                count.lose_life(5)
                explosion.play()
                one_mine.set_explode()
                
        # Check if the player has collided with a missle
        missle_collide = pygame.sprite.spritecollide(player, missles, False)
        for one_missle in missle_collide:
            if not one_missle.is_exploded():
                count.lose_life(10)
                explosion.play()
                one_missle.set_explode()
                
        # Every time the player scores 100 points, randomly choose one submairne and add it to the game
        if count.score_get() > point_check+100:
            point_check = count.score_get()
            sub_add = random.randint(1,5)
            if sub_add == 1:
                submarines.add(gameSprite.Submarine())
                allSprites.add(submarines)
            elif sub_add == 2 or sub_add == 3:
                mine_submarines.add(gameSprite.Mine_Submarine())
                allSprites.add(mine_submarines)
            elif sub_add == 4 or sub_add == 5:
                missle_submarines.add(gameSprite.Missle_Submarine())
                allSprites.add(missle_submarines)
            
            
            
                
                
                
            
        
    
                      
        # R -- REFRESH SCREEN
        allSprites.clear(screen, background)
        mines.clear(screen, background)
        charges.clear(screen, background)
        missles.clear(screen, background)
        
        allSprites.update()
        mines.update()
        charges.update()
        missles.update()
        
        allSprites.draw(screen)
        mines.draw(screen)
        charges.draw(screen)
        missles.draw(screen)
        
        # Check if the player's life point has reached zero or not
        if count.game_lose():
            destory.play()
            player.set_explode()
            
        # Check if the explosion of the play is finished or not
        if player.is_exploded():
            player.kill()
            screen.blit(game_over,(100,200))
            keepGoing = False
            
        
        pygame.display.flip() 
          
    # Create the tkinter window for the player to enter his name
    my_gui = gameSprite.MyGUI(count.score_get())
    
    # Clear everything off the screen
    allSprites.clear(screen, background)
    mines.clear(screen, background)
    charges.clear(screen, background)
    missles.clear(screen, background)
    # Fadeout the music
    pygame.mixer.music.fadeout(2000)
        
        
        

