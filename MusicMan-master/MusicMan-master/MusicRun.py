#Developed by: Timothy Perry, Simone Boyd, Quinn Daugherty, and Paul Tuttle
#Class: CST 205

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
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096) #Initialize the music mixer

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
    
    player = Player()   #Creation of player object

    enemie = Enemie() #Creates game enemies

    rockPlatforms = []
    vinePlatforms = []
    cloudPlatforms = []
    
    mod = [0] #determines how fast scenery moves

     #***Sound Imports******************************************
    #-Music---------------------------------------------------
    Bounce1 = pygame.mixer.Sound('Bouncy2.wav')  #Loads Bouncy 2
    Bounce2 = pygame.mixer.Sound('Bouncy3.wav')  #Loads Bouncy 3
    Eyewalk1 = pygame.mixer.Sound('EyeWalker1.wav')  #Loads Eyewalker1
    Eyewalk2 = pygame.mixer.Sound('EyeWalker2.wav')  #Loads Eyewalker2
    Eyewalk3 = pygame.mixer.Sound('EyeWalker3.wav')  #Loads Eyewalker3
    Walker1 = pygame.mixer.Sound('Walker1.wav')  #Loads Eyewalker1
    Walker2 = pygame.mixer.Sound('Walker2.wav')  #Loads Eyewalker2
    Walker3 = pygame.mixer.Sound('Walker3.wav')  #Loads Eyewalker3

    #--Song Groups------------------------------------------------
    bounceSongs = [Bounce1, Bounce2]    #Holds each characters songs
    eyeSongs = [Eyewalk1, Eyewalk2, Eyewalk3]   #Holds each characters songs
    walkerSongs = [Walker1, Walker2, Walker3]   #Holds each characters songs
    
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

    #---Image Import-----------------------------------

    floor_1 = pygame.image.load("Grass.png").convert()  #loads Grass Platform
    floor_2 = pygame.image.load("Grass.png").convert()  #loads Grass Platform

   
    
    #---Main Program Loop-------------------------------

    while not done:
        # --- Main event loop---------------------------

        for event in pygame.event.get(): # User did something
            if (event.type == pygame.QUIT): # If user clicked close
                pygame.quit()
                done = True # Flag that we are done so we exit this loop

        #--- Creation of platform ------------------------
        global rockPlatforms    # Holds all rock platform objects
        global vinePlatforms    # Holds all vine platform objects
        global cloudPlatforms   # Holds all cloud platform objects
        
        counter1 = 0    #holds current position in vine Platform list
        howManyPlat1 = random.randint(3,6) # determines how many platforms will be generated

        if(len(vinePlatforms) == 0):    # If there are no vine platforms, make more
            for x in range(0, howManyPlat1):
                if(len(vinePlatforms) == 0):
                    vinePlatforms.append(Platform(700, 238,"Platform_02", 26, 90))  #makes first vine object at the beginning right
                else:
                    vinePlatforms.append(Platform(vinePlatforms[counter1 - 1].posX() + 90, 238, "Platform_02", 26, 90))  #makes every other vine attached to it
                counter1 += 1

        counter2 = 0    #holds current position in cloud Platform list
        howManyPlat2 = random.randint(3,6)
        if(len(cloudPlatforms) == 0):    # If there are no cloud platforms, make more
            for x in range(0, howManyPlat2):
                if(len(cloudPlatforms) == 0):
                    cloudPlatforms.append(Platform(700, 114,"Platform_01", 20, 90))  #makes first cloud object at the beginning right
                else:
                    cloudPlatforms.append(Platform(cloudPlatforms[counter2 - 1].posX() + 90, 114, "Platform_01", 20, 90))  #makes every other cloud attached to it
                counter2 += 1

        counter3 = 0    #holds current position in rock Platform list
        howManyPlat3 = random.randint(3,6)
        if(len(rockPlatforms) == 0):    # If there are no rock platforms, make more
            for x in range(0, howManyPlat3):
                if(len(rockPlatforms) == 0):
                    rockPlatforms.append(Platform(700, 351,"Platform_03", 18, 90))  #makes first cloud object at the beginning right
                else:
                    rockPlatforms.append(Platform(rockPlatforms[counter3 - 1].posX() + 90, 351, "Platform_03", 18, 90))  #makes every other cloud attached to it
                counter3 += 1
        #-------------------------------------------------

        onPlatform = [] #Carries each platforms location 

        for x in vinePlatforms:
            onPlatform.append(x.coord())

        for x in cloudPlatforms:
            onPlatform.append(x.coord())

        for x in rockPlatforms:
            onPlatform.append(x.coord())
            
        player.isPlatform(onPlatform, len(vinePlatforms) + len(cloudPlatforms) + len(rockPlatforms))

        #---Updates Screen with new drawings------------
                
        screen.fill(WHITE) #Clears screen to white

        pygame.draw.rect(screen, (100,100,200), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - 150]) #Sky Backdrop
        
        screen.blit(floor_1,(floorX_1, 350))    #Draws Grass to screen
        screen.blit(floor_2,(floorX_2, 350))    #Draws Grass to screen

        #---Menu Loop-----------------------------------Quinn & Simone
    
        while not start and not done:

            #--- Main event loop------------------------
            
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    done = True # Flag that we are done so we exit this loop

           

            if(start == True):
                pygame.mixer.music.stop()
                
            #Animated Title - Simone
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

            #Game Instructions
            text = pygame.image.load("Instructions.png").convert()
            text.set_colorkey(WHITE)

            screen.blit(text, (5, 350))

            #--- Draw character selectors---------------

            char1 = CharacterSelector(200, 300, "Stalk_Walk_")
            char2 = CharacterSelector(350, 300, "Eye_Walk_")
            char3 = CharacterSelector(500, 300, "Blob_Walk_")

            char1.draw(screen)
            char2.draw(screen)
            char3.draw(screen)

            
            button = pygame.mouse.get_pressed() #Checks if mouse button is pressed
            mouse_pos = pygame.mouse.get_pos() #Gets current mouse position
   

            #Starts game when a character is selected - Simone
            if(mouse_pos[0] >= char2.x and mouse_pos[0] <= char2.x + 28):
                if(mouse_pos[1] >= char2.y and mouse_pos[1] <= char2.y + 62):
                    if(button[0]):
                        choice = "Eye_Walk_"
                        start = True

            if(mouse_pos[0] >= char1.x and mouse_pos[0] <= char1.x + 28):
                if(mouse_pos[1] >= char1.y and mouse_pos[1] <= char1.y + 62):
                    if(button[0]):
                        choice = "Stalk_Walk_"
                        start = True

            
            if(mouse_pos[0] >= char3.x and mouse_pos[0] <= char3.x + 28):
                if(mouse_pos[1] >= char3.y and mouse_pos[1] <= char3.y + 62):
                    if(button[0]):
                        choice = "Blob_Walk_"
                        start = True

            pygame.display.flip()

            clock.tick(60)

        
        for x in vinePlatforms:
            x.draw(screen)

        for x in cloudPlatforms:
            x.draw(screen)

        for x in rockPlatforms:
            x.draw(screen)
        
        player.draw(screen) #Draws player to screen

     
        #---Player's Behavior----------------------------

        player.update(mod)


        #---Enemie Behavior----------------------------------

     
        
           
            
            
        #---Platform Behavior----------------------------

        for x in vinePlatforms:
            x.update(mod, vinePlatforms)
        for x in cloudPlatforms:
            x.update(mod, cloudPlatforms)
        for x in rockPlatforms:
            x.update(mod, rockPlatforms)
        
        #---Ground Behavior------------------------------

        floorX_1 -= 1 + mod[0]
        floorX_2 -= 1 + mod[0]

        if(floorX_1 <= -700):   #if floor platform goes out of left screen    
            floorX_1 = floorX_2 + 700     #Attaches floor behind of the previous floor 
        if(floorX_2 <= -700):
            floorX_2 = floorX_1 + 700

        #---Handles all key down events-----------------

        player.handle_keys(mod)
    
        #---Updates the screen with what we've drawn----

        pygame.display.flip()
        
        #---Limit to 60 frames per second---------------

        clock.tick(60)

main()
