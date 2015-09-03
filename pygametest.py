# Pygametest.py
# Created by Justin Nguyen

import pygame, sys, random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
TEXTDISPLAYX = 220
TEXTDISPLAYY = 440
FALLSPEED = 1
MAXSTRINGCOUNT = 5
WORDS = ['cat', 'hat', 'xylophone', 'onomatopoeia', 'pyrophobic', 'scared', 'melee']

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BGCOLOR = WHITE
strX = random.randint(0, WINDOWWIDTH)
strY = 0

def main():
    global fpsClock, DISPLAYSURF
    pygame.init()
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Typing Game')
    DISPLAYSURF.fill(BGCOLOR)
    inputStr = ""
    pygame.key.set_repeat(200, 50)
    
    testStr = 'Hello World'
    fontObj = pygame.font.Font(pygame.font.get_default_font(), 20)
    textSurfaceObj = fontObj.render(testStr, True, BLACK, BGCOLOR)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 159)
    
    while True: # main game loop
        DISPLAYSURF.fill(BGCOLOR)
        groundRect = (0, 400, 640, 5)
        pygame.draw.rect(DISPLAYSURF, BLACK, groundRect) 
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key ==
K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(inputStr) > 0:
                        inputStr = inputStr[:-1]
                    else:
                        inputStr = ""
                #elif event.key == K_RETURN:
                    
                else:
                    inputStr = inputStr + event.unicode

        displayFont = pygame.font.Font(None, 20)
        textDisplay = displayFont.render(inputStr, True, BLACK, BGCOLOR)
        displayRect = textDisplay.get_rect()
        centeredRect = displayRect.move(TEXTDISPLAYX, TEXTDISPLAYY)
        DISPLAYSURF.blit(textDisplay, (TEXTDISPLAYX, TEXTDISPLAYY))
        pygame.draw.rect(DISPLAYSURF, BLACK, centeredRect, 1)
        pygame.display.update()
        fpsClock.tick(FPS)

class targetString(object):
    def __init__(self):
        self.word = random.choice(WORDS)
        self.alive = True

def initHUD():
    livesString = "Lives(): "
    LIVES = 5
    levelString = "Level: "
    pointsString = "Points: "
    wordsLeftString = "Word(s) Left: "
    
    groundRect = (0, 400, 640, 5)
    pygame.draw.rect(DISPLAYSURF, BLACK, groundRect)
    
        
#def generateNextString():
    
main()
