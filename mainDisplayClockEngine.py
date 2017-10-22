from main import *
#from pygame import *
import threading
from time import time

kmhVariableAngle =0

def setScreen(oldscreen):
    global screen
    screen = oldscreen

def setKmhValue(oldKmhValue):
    global kmhVariable
    kmhVariable = oldKmhValue

def setRPMValue(oldRpmValue):
    global rpmVariable
    rpmVariable = oldRpmValue





class displayMainClock(threading.Thread):
    def __init__(self):
        super(displayMainClock, self).__init__()
        threading.Thread.__init__(self)


    def run(self):
        clock = pygame.time.Clock()

        kmhImage = pygame.image.load('resources/kmh.png')
        kmhImage = pygame.transform.scale(kmhImage, (400, 400))

        rpmmImage = pygame.image.load('resources/rpmm.png')
        rpmmImage = pygame.transform.scale(rpmmImage, (400, 400))

        kmhAcImage = pygame.image.load('resources/ac.png')
        kmhAcImage = pygame.transform.scale(kmhAcImage, (400, 400))


        while 1:

            screen.blit(kmhImage, (0, 300))
            screen.blit(rpmmImage, (870, 300))



            #pygame.display.flip()
