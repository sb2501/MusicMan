import random
import pygame

GROUND = 300
WHITE = (255,255,255)

class Player(object):

    def __init__(self, option): #Constructor
        self.image = pygame.image.load(option + "1.png").convert()  #Loads Character
        self.image.set_colorkey(WHITE)  #Sets color to turn transparent
        self.x = 140 # x position object is drawn at
        self.y = 300 # y position object is drawn at
        self.width = 28 # width of pic
        self.height = 62 # height of pic
        self.stat = 1 # counter for update()
        self.walk = 12 # Controls how fast animation loops
        self.isJump = False #Controls Jump algorithm
        self.stable = False

    def isPlatform(self, collision):
        #Collion: multidimentional [3][x,y,width]
        if((self.y + self.height) == collision[0][1]):
            if(self.x >= collision[0][0] and self.x <= (collision[0][0] + collision[0][2])):
                self.stable = True
                return
        self.stable = False
        

    def handle_keys(self, mod):
        #Handles all key down events

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): #moves character to the right 
            if(mod[0] < 6):
                mod[0] += 1
                
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): #moves character to the left
            if(mod[0] > 0):
                mod[0] -= 1

        #---Jumping---------------------------- 

        if ((keys[pygame.K_w] or keys[pygame.K_UP]) and self.y == GROUND):  #Checks if player is currently jumping
            self.isJump = True

        if(self.y == 238 - self.height): # Stops character at first platform
            self.isJump = False
            
        if (self.isJump): #jumps character
            self.y -= 2
            
        if ((self.isJump == False and self.y != GROUND) and not (self.stable)): #Bring player to the ground
            self.y += 2
                
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y)) #draws player to screen

    def update(self, mod, option):
        if (self.stat < self.walk * 2):    #draws first animation
            self.image = pygame.image.load(option + "1.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 2 and self.stat < self.walk * 4):   #draws second animation
            self.image = pygame.image.load(option + "2.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 4 and self.stat < self.walk * 6):  #draws third animation
            self.image = pygame.image.load(option + "3.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 6 and self.stat < self.walk * 8):  #draws fourth animation
            self.image = pygame.image.load(option + "4.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 8 and self.stat < self.walk * 10):  #draws fourth animation
            self.image = pygame.image.load(option + "5.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 10 and self.stat < self.walk * 12):  #draws fourth animation
            self.image = pygame.image.load(option + "6.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 12 and self.stat < self.walk * 14):  #draws fourth animation
            self.image = pygame.image.load(option + "7.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 14 and self.stat < self.walk * 16):  #draws fourth animation
            self.image = pygame.image.load(option + "8.png").convert()
            self.image.set_colorkey(WHITE)

        self.stat += 5 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > self.walk * 16):   #loops back to beginning animation
            self.stat = 1

class Platform(object):
    def __init__(self, xPos, yPos, image, h, l):
        self.x = xPos # x position of platform
        self.y = yPos # y position of platform
        self.image = pygame.image.load(image + ".png").convert()
        self.image.set_colorkey(WHITE)
        self.height = h # height of picture
        self.length = l # length of picture
        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y)) #draws platform to screen

    def update(self, mod):
        self.x -= 1 + mod[0] #how fast plaform is moving

        if(self.x < -100): #if platform goes out of screen, re-appear on right side
            self.x = 700

    def coord(self):
        return [self.x, self.y, self.length]


class CharacterSelector(object):
    def __init__(self, xPos, yPos, option):
        self.x = xPos
        self.y = yPos
        self.stat = 1 # counter for update()
        self.walk = 12 # Controls how fast animation loops
        self.image = pygame.image.load(option + "1.png").convert()
        self.image.set_colorkey(WHITE)
              
        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        

    def update(self, mod, option):
        if (self.stat < self.walk * 2):    #draws first animation
            self.image = pygame.image.load(option + "1.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 2 and self.stat < self.walk * 4):   #draws second animation
            self.image = pygame.image.load(option + "2.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 4 and self.stat < self.walk * 6):  #draws third animation
            self.image = pygame.image.load(option + "3.png").convert()
            self.image.set_colorkey(WHITE)
            
        if (self.stat >= self.walk * 6 and self.stat < self.walk * 8):  #draws fourth animation
            self.image = pygame.image.load(option + "4.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 8 and self.stat < self.walk * 10):  #draws fourth animation
            self.image = pygame.image.load(option + "5.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 10 and self.stat < self.walk * 12):  #draws fourth animation
            self.image = pygame.image.load(option + "6.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 12 and self.stat < self.walk * 14):  #draws fourth animation
            self.image = pygame.image.load(option + "7.png").convert()
            self.image.set_colorkey(WHITE)

        if (self.stat >= self.walk * 14 and self.stat < self.walk * 16):  #draws fourth animation
            self.image = pygame.image.load(option + "8.png").convert()
            self.image.set_colorkey(WHITE)

        self.stat += 5 + mod[0] #how fast animation moves plus speed of character
        
        if (self.stat > self.walk * 16):   #loops back to beginning animation
            self.stat = 1


