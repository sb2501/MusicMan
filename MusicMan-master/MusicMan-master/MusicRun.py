# Import a library of functions called 'pygame'
import os
import pygame
import random
from Draw import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 60, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 255)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
GROUND = 250 #pixel ground level

mod = 0
        
def main():
    
    pygame.init()# Initialize the game engine

    size = (700, 500)   #Window Size
    screen = pygame.display.set_mode(size)  #Window Creation
    pygame.display.set_caption("MusicRun")  #Displays Window Title

    
    done = False # Loop until the user clicks the close button.
    start = False
    choice = "Eye_Walk_" #Initial character selection

    time = 0
    total = 60

    clock = pygame.time.Clock() # Used to manage how fast the screen updates
    
    velocity = 4 #speed of character

    cloudX, cloudY = SCREEN_WIDTH, random.randrange(10, 100) #Starting pos of clouds
    floorX_1, floorX_2 = 0, 700 #Placement of grass running surface
    

    platform1 = Platform(150, 238,"Platform_02", 26, 90)    #Creates Vine Platform Object
    platform2 = Platform(150, 114,"Platform_01", 20, 90)    #Creates Cloud Platform Object
    platform3 = Platform(150, 351,"Platform_03", 18, 90)    #Creates Stone Platform Object
    
    mod = [0] #determines how fast scenery moves

    #***Sound Imports******************************************
    #-Music---------------------------------------------------
    pygame.mixer.music.load('A Wish.ogg')   #Loads song into pygame
    
    #-Sound Effects-------------------------------------------
    BirdSquark = pygame.mixer.Sound('Bird squark2.wav')    #Loads sound effect.
    Cat = pygame.mixer.Sound('CAT03.wav')    #Loads cat sound effect.
    ComicMosquito = pygame.mixer.Sound('Comic mosquito.wav')    #Loads mosquito sound effect.
    Humanoid = pygame.mixer.Sound('Humanoid.wav')    #Loads humanoid sound effect.
    Move1 = pygame.mixer.Sound('Move1.wav')    #Loads move1 sound effect.
    Move2 = pygame.mixer.Sound('Move2.wav')    #Loads move2 sound effect.
    Slurp = pygame.mixer.Sound('Slurp1.wav')    #Loads sound effect.
    Slurp2 = pygame.mixer.Sound('Slurp2.wav')    #Loads sound effect.
    SPLODGE = pygame.mixer.Sound('SPLODGE.wav')    #Loads sound effect.
    TimeMachine = pygame.mixer.Sound('Time machine loop2.wav')    #Loads sound effect.
    Whoosh = pygame.mixer.Sound('WHOOSH08.WAV')    #Loads sound effect.
    Zingle = pygame.mixer.Sound('ZINGLE.WAV')    #Loads sound effect.


    #jump_sound = pygame.mixer.Sound("spin_jump.wav") #Jump Sound

    floor_1 = pygame.image.load("Grass.png").convert()  #loads Grass Platform
    floor_2 = pygame.image.load("Grass.png").convert()  #loads Grass Platform

    #---Main Program Loop-------------------------------

    while not done:
        # --- Main event loop---------------------------

        for event in pygame.event.get(): # User did something
            if (event.type == pygame.QUIT): # If user clicked close
                done = True # Flag that we are done so we exit this loop

        onPlatform = [] #Carries each platforms location 
        onPlatform.append(platform1.coord())
        onPlatform.append(platform2.coord())
        onPlatform.append(platform3.coord())
        player.isPlatform(onPlatform)

        #---Updates Screen with new drawings------------
                
        screen.fill(WHITE) #Clears screen to white

 
        pygame.draw.rect(screen, (100,100,200), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 150]) #Sky Backdrop
        
        screen.blit(floor_1,(floorX_1, 350))    #Draws Grass to screen
        screen.blit(floor_2,(floorX_2, 350))    #Draws Grass to screen

     


        #---Menu Loop-----------------------------------
    
        while not start and not done:

            #--- Main event loop------------------------
            
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop

            #Animated Title
            if(time < total - 40):
                image = pygame.image.load("Title1.png").convert()
                image.set_colorkey(WHITE)

                screen.blit(image,(150,50))
            if(time > total - 40):
                image = pygame.image.load("Title2.png").convert()
                image.set_colorkey(WHITE)

                screen.blit(image,(150,50))
            if(time >= total - 30):
                image = pygame.image.load("Title3.png").convert()
                image.set_colorkey(WHITE)

                screen.blit(image,(150,50))
            if(time == total):
                time = 0

            time += 5

            #--- Draw character selectors---------------

            char1 = CharacterSelector(200, 300, "Stalk_Walk_")
            char2 = CharacterSelector(350, 300, "Eye_Walk_")
            char3 = CharacterSelector(500, 300, "Blob_Walk_")

            char1.draw(screen)
            char2.draw(screen)
            char3.draw(screen)

           
            button = pygame.mouse.get_pressed() #Checks if mouse button is pressed
            mouse_pos = pygame.mouse.get_pos() #Gets current mouse position
   

            #Starts game when a character is selected
            if(mouse_pos[0] >= char2.x and mouse_pos[0] <= char2.x + 28):
                if(mouse_pos[1] >= char2.y and mouse_pos[1] <= char2.y + 62):
                    if(button[0]):
                        Eyewalk1 = pygame.mixer.Sound('EyeWalker1.wav')  #Loads Eyewalker1 music loop
                        Eyewalk2 = pygame.mixer.Sound('EyeWalker2.wav')  #Loads Eyewalker2 music loop
                        Eyewalk3 = pygame.mixer.Sound('EyeWalker3.wav')  #Loads Eyewalker3 music loop
                        musicSet = [Eyewalk1, Eyewalk2, Eyewalk3]
                        choice = "Eye_Walk_"
                        start = True

            if(mouse_pos[0] >= char1.x and mouse_pos[0] <= char1.x + 28):
                if(mouse_pos[1] >= char1.y and mouse_pos[1] <= char1.y + 62):
                    if(button[0]):
                        Walker1 = pygame.mixer.Sound('Walker1.wav')  #Loads Eyewalker1 music loop
                        Walker2 = pygame.mixer.Sound('Walker2.wav')  #Loads Eyewalker2 music loop
                        Walker3 = pygame.mixer.Sound('Walker3.wav')  #Loads Eyewalker3 music loop
                        musicSet = [Walker1, Walker2, Walker3]
                        choice = "Stalk_Walk_"
                        start = True
            
            if(mouse_pos[0] >= char3.x and mouse_pos[0] <= char3.x + 28):
                if(mouse_pos[1] >= char3.y and mouse_pos[1] <= char3.y + 62):
                    if(button[0]):
                        Bounce1 = pygame.mixer.Sound('Bouncy2.wav')  #Loads Bouncy 2 music loop
                        Bounce2 = pygame.mixer.Sound('Bouncy3.wav')  #Loads Bouncy 3 music loop
                        musicSet = [Bounce1, Bounce2]
                        choice = "Blob_Walk_"
                        start = True

            if (start = true)
                player = Player(choice, musicSet)   #Creation of player object

            pygame.display.flip()

            clock.tick(60)
                


        platform1.draw(screen)  #Draws Vine platform
        platform2.draw(screen)  #Draws Cloud platform
        platform3.draw(screen)  #Draws Stone Platform
        player.draw(screen) #Draws player to screen

        #---Player's Behavior----------------------------

        player.update(mod, choice)

        #---Platform Behavior----------------------------

        platform1.update(mod)
        platform2.update(mod)
        platform3.update(mod)
        
        #---Ground Behavior------------------------------

        floorX_1 -= 1 + mod[0]
        floorX_2 -= 1 + mod[0]

        if(floorX_1 <= -700):   #if floor platform goes out of left screen    
            floorX_1 = 700     #Returns floor platform to the right of the screen
        if(floorX_2 <= -700):
            floorX_2 = 700

        #---Handles all key down events-----------------

        player.handle_keys(mod)
    
        #---Updates the screen with what we've drawn----

        pygame.display.flip()
        
        #---Limit to 60 frames per second---------------

        clock.tick(60)

    pygame.quit()
    
main()
