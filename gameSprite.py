'''Auther            : HeFengChen
   Date last modified: Apr 24 2011
   Description       : The program contains all sprite classes that are needed for
                       the game.'''


import pygame,random,Tkinter
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the player'''
    def __init__(self,screen):
        '''This initializer takes no parameters. It will load all the images that are needed for later
        use. It also sets the potsition of the player sprite. The state of the sprite of whether it has
        exploded or not is also defined in this method.'''
        
        pygame.sprite.Sprite.__init__(self)
        
        # import and organize all the images needed
        self.image = pygame.image.load("Picture/ship.png")
        self.__explode = [pygame.image.load("Picture/explosion1.png"),pygame.image.load("Picture/explosion2.png"),pygame.image.load("Picture/explosion3.png"),pygame.image.load("Picture/explosion4.png"),pygame.image.load("Picture/explosion5.png"),pygame.image.load("Picture/explosion6.png"),pygame.image.load("Picture/explosion7.png"),pygame.image.load("Picture/explosion8.png"),pygame.image.load("Picture/explosion9.png"),pygame.image.load("Picture/explosion10.png"),pygame.image.load("Picture/explosion11.png"),pygame.image.load("Picture/explosion12.png")]
        self.__is_explode = False
        self.__number = 0 
        self.__explode_finish = False
           
        # Set the rect attributes for the Player
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_width()/2
        self.rect.top = 60
        self.__dx = 0
        
    def change_direction(self,xy_value):
        '''This method takes a (x,y) tuple as a parameter, extracts the x element from it, and uses this 
        to set the players y direction. The method does not return anything'''
        self.__dx = (xy_value[0])*4
        
    def set_explode(self):
        '''This method takes no parameters. It sets the exploding state of the sprite to true which means
        the sprite will explode. The method does not return anything'''
        self.__is_explode = True
        
    def is_exploded(self):
        '''This method takes no parameters. It returns a boolean value of whether the explosion has
        finished or not.'''
        return self.__explode_finish
        
    def update(self):
        '''This method will be called automatically to reposition the 
        player sprite on the screen. If the exploding state is true, then the explosion animation will be
        played and kill the sprite when it finishes. The method does not return anything'''
        
        # Check the if player has exploded or not
        if self.__is_explode:
            
            # if true, play the explosion animation and then kill the sprite
            self.image = self.__explode[self.__number]
            self.__number += 1
            if self.__number > 11:
                self.__explode_finish = True
                self.__is_explode = False
                self.kill()
                
        elif ( ( self.rect.left >  0) and ( self.__dx <= 0 )) or(( self.rect.right < 640 ) and ( self.__dx >= 0 )):
            # Otherwise, reposition the sprite according to the input            
            self.rect.left +=  self.__dx
            
            
class Submarine(pygame.sprite.Sprite):
    '''This class defines the sprite for the submarine'''
    def __init__(self):
        '''This initializer takes no parameters. It will load all the images that are needed for later
        use. It also sets the potsition of the submarine sprite. The state of the sprite of whether it has
        exploded or not is also defined in this method and the range of activity of the submarine'''
        
        pygame.sprite.Sprite.__init__(self)
        
        # import and organize all the images needed
        self.__right = pygame.image.load("Picture/sub1_right.png")
        self.__left = pygame.image.load("Picture/sub1_left.png")
        self.__explode = [pygame.image.load("Picture/explosion1.png"),pygame.image.load("Picture/explosion2.png"),pygame.image.load("Picture/explosion3.png"),pygame.image.load("Picture/explosion4.png"),pygame.image.load("Picture/explosion5.png"),pygame.image.load("Picture/explosion6.png"),pygame.image.load("Picture/explosion7.png"),pygame.image.load("Picture/explosion8.png"),pygame.image.load("Picture/explosion9.png"),pygame.image.load("Picture/explosion10.png"),pygame.image.load("Picture/explosion11.png"),pygame.image.load("Picture/explosion12.png")]
        
        self.__is_explode = False
        self.depth_range = [95,233]
        
        
        # Set the attributes for the sprite
        self.reset()
        
    def set_released(self):
        '''This method takes no parameters. It sets the  released attribut to a false value which means
        that the submarine will not fire anymore. This method does not return anything.'''
        
        self.__released = 0
    
    def is_released(self):
        '''This method takes no parameters. It returns the self.released attribute, showing whether or not 
        this submarine has attacked'''
        
        return self.__released
            
    def set_explode(self):
        '''This method takes no parameters. It sets the exploding state of the sprite to true which means
        the sprite go through explode animation. The method does not return anything'''
        
        self.__is_explode = True
        
    def image_switch_2(self):
        '''This method takes no parameters. This method sets the image attributes and activity range for a
        second type of submarine. The method does not return anything.'''
        
        self.__right = pygame.image.load("Picture/sub2_right.png")
        self.__left = pygame.image.load("Picture/sub2_left.png")
        self.depth_range = [243,351]
        
    def image_switch_3(self):
        '''This method takes no parameters. This method sets the image attributes and activity range for a
        third type of submarine. The method does not return anything.'''
        
        self.__right = pygame.image.load("Picture/sub3_right.png")
        self.__left = pygame.image.load("Picture/sub3_left.png")
        self.depth_range = [361,450]
        
    def reset(self):
        '''This method takes no parameters. This method sets all the important attributes for the sprite,
        including the direction, speed, depth and starting sides. The method does not return anything.'''
        
        direction = random.randint(0,1)
        self.__released = random.randint(0,2)
        self.__number = 0
        # set the image, speed and rect attributes for the submarine according to its direction 
        if direction:
            self.image = self.__right
            self.rect = self.image.get_rect()
            self.rect.right = 0
            self.__dx = random.randint(2,5)
        else:
            self.image = self.__left
            self.rect = self.image.get_rect()
            self.rect.left = 640
            self.__dx = -(random.randint(2,5))
        self.rect.top = random.randint(self.depth_range[0],self.depth_range[1])
        
    def update(self):
        '''This method will be called automatically to reposition the 
        submarine sprite on the screen. If the exploding state is true, then the explosion animation will be
        played and reset the sprite when it finishes. The method does not return anything'''

        # Check if ball have reached the top or bottom of the court. 
        if ( ( self.rect.right >  0) and ( self.__dx < 0 )) or(( self.rect.left < 640 ) and ( self.__dx > 0 )):
            if self.__is_explode:
                self.image = self.__explode[self.__number]
                self.__number += 1
                if self.__number > 11:
                    self.reset()
                    self.__is_explode = False
            else:
                self.rect.left +=  self.__dx   
        else:
            self.reset()
            
            
    
class Mine_Submarine(Submarine):
    '''This class defines the sprite for the mine_submarine'''
    def __init__(self):
        '''This initializer takes no parameters. It will load all the images that are needed for later
        use. It also sets the potsition of the submarine sprite. The state of the sprite of whether it has
        exploded or not is also defined in this method and the range of activity of the submarine'''
        
        Submarine.__init__(self)
        self.image_switch_2()
        self.reset()
        
        
        
class Missle_Submarine(Submarine):
    '''This class defines the sprite for the missle submarine.'''
    def __init__(self):
        '''This initializer takes no parameters. It will load all the images that are needed for later
        use. It also sets the potsition of the submarine sprite. The state of the sprite of whether it has
        exploded or not is also defined in this method and the range of activity of the submarine'''
        
        Submarine.__init__(self)
        self.image_switch_3()
        # this attribute set from where the submarine will launch the missle
        self.__fire_range = random.randint(40,600)
        self.reset()
        
    def get_fire_range(self):
        '''This mathod takes not parameters. It returns the firing range of the submarine.'''

        return self.__fire_range
    

                

                
class Mine(pygame.sprite.Sprite):
    '''This class defines the sprite for the water mines.'''
    def __init__(self,screen,top,centerx):
        '''This initializer takes screen, rect.top of the submarine and rect.centerx of the submairne as
        parameters. It will load all the images that are needed for later
        use. It also sets the potsition of the mine sprite. The state of the sprite of whether it has
        exploded or not is also defined in this method.'''
        
        pygame.sprite.Sprite.__init__(self)
        
        # import and organize all the images needed
        self.image = pygame.image.load("Picture/mine.png")
        self.__explode = [pygame.image.load("Picture/small_ex1.png"),pygame.image.load("Picture/small_ex2.png"),pygame.image.load("Picture/small_ex3.png"),pygame.image.load("Picture/small_ex4.png"),pygame.image.load("Picture/small_ex5.png"),pygame.image.load("Picture/small_ex6.png"),pygame.image.load("Picture/small_ex7.png")]
        self.__is_explode = False
        self.__number = 0 
        self.__time = 0

           
        # Set the rect attributes for the Mine
        self.rect = self.image.get_rect()
        self.rect.top = top-10
        self.rect.centerx = centerx
        self.__dy = -3
      
        
    def is_exploded(self):
        '''This method takes no parameters. It returns a boolean value of whether the mine has
        exploeded or not.'''
        
        return self.__is_explode 
    
    def set_explode(self):
        '''This method takes no parameters. It sets the exploding state of the sprite to true which means
        the sprite will go through explode animation. The method does not return anything'''
        
        self.__is_explode = True
        
    def update(self):
        '''This method will be called automatically to reposition the 
        mine sprite on the screen. If the exploding state is true, then the explosion animation will be
        played and kill the sprite when it finishes. The method does not return anything'''
        
        # check if the mine is below water line
        if (  self.rect.top < 480) and ( self.rect.top > 86 ) :
            
            # if the mine has exploded, then go through explosion animation
            if self.__is_explode:
                self.rect.top -= 5
                self.image = self.__explode[self.__number]
                self.__number += 1
                if self.__number > 6:
                    self.kill()
            # if the mine didnt explode, then add dy to its rect.top
            else:
                self.rect.top += self.__dy
                
        # if the mine has reach the water line
        else:
            # if the mine has exploded, then go through explosion animation
            if self.__is_explode:
                self.rect.top -= 5
                self.image = self.__explode[self.__number]
                self.__number += 1
                if self.__number > 6:
                    self.kill()
            # make the mine stay for 1 second on the waterline then disappear
            self.__time += 1
            if self.__time == 60:
                self.kill()
                
            
          
            
class Depth_charge(pygame.sprite.Sprite):
    '''This class defines the sprite for the depth_charge'''
    def __init__(self,screen,centerx):
        '''This initializer takes screen and centerx of the ship as parameters. It will load all the
        images that are needed for later use. It also sets the potsition of the depth charge sprite. 
        This method does not return anything.'''
        
        pygame.sprite.Sprite.__init__(self)
        
        # import and organize all the images needed
        self.__picture = [pygame.image.load("Picture/bomb1.png"),pygame.image.load("Picture/bomb1.png"),pygame.image.load("Picture/bomb2.png"),pygame.image.load("Picture/bomb2.png"),pygame.image.load("Picture/bomb3.png"),pygame.image.load("Picture/bomb3.png")]
        self.__image_num = 0
        self.image = self.__picture[self.__image_num]
       

           
        # Set the rect attributes for the Depth_charge
        self.rect = self.image.get_rect()
        self.rect.top = 85
        self.rect.centerx = centerx
        self.__dy = +3
    
    
        
    def update(self):
        '''This method will be called automatically to reposition the 
        depth charge sprite on the screen. The sprite will kill itself when it goes out of the boundry.
        The method does not return anything'''
        
        # Check if the depth charge is within the screen. 
        if (  self.rect.top < 480) :
            # if true, add dy to its rect.top and play the animation
            self.rect.top += self.__dy
            self.__image_num += 1
            if self.__image_num > 5:
                self.__image_num = 0
            self.image = self.__picture[self.__image_num]
            
        else:
            # kill the sprite once it goes out of the screen parameter
            self.kill()
            
            
            
class Missle(pygame.sprite.Sprite):
    '''This class defines the sprite for the missle'''
    def __init__(self,top,centerx,destoryer_centerx,destoryer_left,destoryer_right):
        '''This initializer takes the rect.top of the submarine, rect.centerx of the subamrine, the
        centerx of the player, the rect.left and rect.right of the player as parameters. It will load all the
        images that are needed for later use. It also sets the potsition and speed of the missle sprite. 
        This method does not return anything.'''
      
        pygame.sprite.Sprite.__init__(self)
        
        # import and organize all the images needed
        self.__left = pygame.image.load("Picture/missle_left.png")
        self.__right = pygame.image.load("Picture/missle_right.png")
        self.__up = pygame.image.load("Picture/missle_up.png")
        self.__explode = [pygame.image.load("Picture/small_ex1.png"),pygame.image.load("Picture/small_ex2.png"),pygame.image.load("Picture/small_ex3.png"),pygame.image.load("Picture/small_ex4.png"),pygame.image.load("Picture/small_ex5.png"),pygame.image.load("Picture/small_ex6.png"),pygame.image.load("Picture/small_ex7.png")]
        self.__is_explode = False
        self.__number = 0 
        
        self.__target_centerx = destoryer_centerx
        self.__target_left = destoryer_left
        self.__target_right = destoryer_right
        self.__top = top
        self.__centerx = centerx
        self.image = self.__up
           
        # Set the rect attributes for the Missle
        self.rect = self.image.get_rect()
        self.rect.top = top-10
        self.rect.centerx = centerx
        self.__dy = -5
       
        
    def set_explode(self):
        '''This method takes no parameters. It sets the exploding state of the sprite to true which means
        the sprite will go through explode animation. The method does not return anything'''
        
        self.__is_explode = True
        
    def is_exploded(self):
        '''This method takes no parameters. It returns a boolean value of whether the missle has
        exploeded or not.'''
        
        return self.__is_explode 
   
        
    def update(self):
        '''This method will be called automatically to reposition the 
        mine sprite on the screen. If the exploding state is true, then the explosion animation will be
        played and kill the sprite when it finishes. The method does not return anything'''

        # Check if missle is with the screen
        if (  self.rect.top < 480) and ( self.rect.top > 0 ) and (self.rect.left > 0) and (self.rect.right < 640):
            # check if exploding state is true. if so play the animation and kill
            if self.__is_explode:
                self.rect.top -= 5
                self.image = self.__explode[self.__number]
                self.__number += 1
                if self.__number > 6:
                    self.kill()
                
            # check if missle has reached the bottom of the player, aim the missle at the player
            else:
                if (self.rect.centerx > self.__target_left+10) and (self.rect.centerx < self.__target_right-10):
                    self.image = self.__up
                    self.__dx = 0
                elif self.rect.centerx < self.__target_centerx:
                    self.image = self.__right
                    self.__dx = 7
                elif self.rect.centerx > self.__target_centerx:
                    self.image = self.__left
                    self.__dx = -7
                self.rect.left += self.__dx
                self.rect.top += self.__dy
            
        # kill the sprite if it goes out of the screen
        else:
            self.kill()
            
            
            
class Count(pygame.sprite.Sprite):
    '''This class defines the sprite for the counter'''
    def __init__(self):
        '''This initializer takes no parameters. It will set the font and initial values for labels that
        will be displayed on the screen. This method does not return anything.'''
        
        pygame.sprite.Sprite.__init__(self)
        
        # Set the font attributes for the label 
        self.__font = pygame.font.Font("font.ttf",20)
        self.__player_life = 100
        self.__player_score = 0
    
    def lose_life(self,point):
        '''This method takes a int value as parameter. It will then subtract the value from the player's
        life point. This function does not return anything.'''
        self.__player_life -= point
        
    def add_score(self,score):
        '''This method takes a int value as parameter. It will then add the value to the player's
        score point. This function does not return anything.'''
        
        self.__player_score += score
        
    def score_get(self):
        '''This function takes no parameters. It returns the '''
        
        return self.__player_score
        
    def game_lose(self):
        '''This method takes no parameter. It checks the value of the player's life point. if the
        life point is greater thatn 0, a true value will be returned, otherwise, a false value will
        be returned.'''
        if self.__player_life <= 0:
            return 1
        else:
            return 0
        
    def update(self):
        '''This method will be called automatically to update the content in the label object.
        It also sets the rect of the label object on a fixed point. The method does not return anything'''
        
        message = "Life: %d    Score: %d       Ready:" %(self.__player_life,self.__player_score)
        self.image = self.__font.render(message,1,(0,0,0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (240,30)
        
        
class Status_Bar(pygame.sprite.Sprite):
    '''This class defines the sprite for the status bar.'''
    def __init__(self):
        '''This initializer takes no parameters. It calls the reset function to set all the necessary
        attributes for the game. This method does not return anything.'''
        
        pygame.sprite.Sprite.__init__(self)
        self.reset()
        
    def reset(self):
        '''This method takes no parameters. It sets all the necessary attributes for the game.
        This method does not return anything.'''
        
        self.image = pygame.Surface((0,10))
        self.__width = 0
        self.__ready = False
        
        # Set the rect attributes for the sptire
        self.rect = self.image.get_rect()
        self.rect.left = 450
        self.rect.top = 24
        
    def is_ready(self):
        '''This method takes no parameters. It returns a boolean value indicating whether the status bar has
        reached its full length or not.'''
        
        return self.__ready
    
    def update(self):
        '''This method automatically updates the new size of the status bar. If it has rechead its full
        length, it will stop extending and the ready attribute will become true. This method does not
        return anything.'''
        
        # check if the bar has extended to its full length.
        if self.__width < 150:
            self.__width += 10
            self.image = pygame.Surface((self.__width,10))
            self.image.fill((255,0,0))
            
        # if the bar is in full length, set the ready attribute to true
        else:
            self.__ready = True
            
            

            
            
class Label(pygame.sprite.Sprite):
    '''This class defines the sprite for the label'''
    def __init__(self, message, xy_center):
        '''This initializer takes the message and position as parameters. It will set the font, messages
        color and positions for labels that will be displayed on the screen. This method does not return
        anything.'''
        
        pygame.sprite.Sprite.__init__(self)
        
        self.__font = pygame.font.Font("BURNSTOW.ttf", 60)
        self.__message = message
        self.image = self.__font.render(self.__message, 1, (255, 255, 255))
        self.__color =(255,255,255)
        
        # Set the rect attributes for the sptire
        self.rect = self.image.get_rect()
        self.rect.center = xy_center
         
 
        
    def color_change(self):
        '''This method takes no parameters. It changes the RGB value of the label sprite. This function
        does not return anything.'''
        
        self.__color =(255,0,0)
        
    def update(self): 
        '''This method automatically the color of the label sprite, then sets sptire back to its default
        color.'''
        
        self.image = self.__font.render(self.__message, 1,self.__color) 
        self.__color =(255,255,255)
                 

        
        
        
        
class Hall_of_fame(pygame.sprite.Sprite):
    '''This class defines the sprite for the hall of fame'''
    def __init__(self,message,xy_center):
        '''This initializer takes the message and position as parameters. It will set the font, messages
        and positions for labels that will be displayed on the screen. This method does not return
        anything. This method is specially made for HallofFame because its labels do not need to be
        updated.'''
        
        pygame.sprite.Sprite.__init__(self)
    
        self.__font = pygame.font.SysFont("none", 30)
        self.image = self.__font.render(message, 1, (225, 225, 225))
        
        # Set the rect attributes for the sptire
        self.rect = self.image.get_rect()
        self.rect.left = xy_center[0]
        self.rect.top = xy_center[1]
        
        

        
class MyGUI:
    '''This class defines the sprite for the GUI window'''
    def __init__(self,score):
        '''This initializer takes score value as a parameter. It creates a tkinter window for the user to
        enter their score. This function does not return anything.'''
        
        self.main_window = Tkinter.Tk()
        
        self.score = score
        
        # Create two frames
        self.frame_number1 = Tkinter.Frame()
        self.frame_number2 = Tkinter.Frame()
       
        
        # Create a label widget for the first row
        self.label =  Tkinter.Label(self.frame_number1,text='Please enter your user name and click Enter. Close window to exit.')
        
        self.label.pack()
        
        # Create an input widget for the second row
        self.prompt_name = Tkinter.Label(self.frame_number2,text = 'User Name:')
        self.name_entry = Tkinter.Entry(self.frame_number2,width=30)
        
        self.prompt_name.pack(side='left')
        self.name_entry.pack(side='left')
        
        # Create a button widget and pack it beside the input widget
        self.story_button = Tkinter.Button(self.frame_number2,text='Enter',command = self.record)
        self.story_button.pack(side='left')
        
        # Place the frames in their allocated positions
        self.frame_number1.pack(anchor='w')
        self.frame_number2.pack(anchor='w')
       
        
        Tkinter.mainloop()
        
    def record(self):
        '''This method takes no parameters. It is called when the button is pressed. It saves the playes's
        user name and score to to txt file. This method does not return anything.'''
        
        # create the file if it doesn't exist
        file_HallOfFame = open("Document/HallOfFame.txt","a")
        file_HallOfFame.close()
     
        # open the file HallOfFame
        file_HallOfFame = open("Document/HallOfFame.txt","a")
        
        # write player's name and score into HallOfFame
        name = self.name_entry.get()
        file_HallOfFame.write(name + ":" + str(self.score) +"\n")
        file_HallOfFame.close()
        
        # save the score to a seperate file for later use
        file_Score = open("Document/Score.txt","a")
        file_Score.write(str(self.score) +"\n")
        file_Score.close()
        
        
        
class Cursor(pygame.sprite.Sprite):
    '''This class defines the sprite for the cursor'''
    def __init__(self):
        '''This initializer takes no parameters. It will set the image and rect for cursor that will
        be displayed on the screen. This method does not return anything.'''
        
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the cursor
        self.image = pygame.image.load("Picture/Cursor.png")
        self.rect = self.image.get_rect()
         
    def update(self):
        '''This method automatically reposition the cursor on the screen. This function does not return
        anything.'''
        
        # Move the center of the cursor to where the mouse is pointing
        self.rect.center = pygame.mouse.get_pos()

        
    
        
                
            
          