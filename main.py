import pygame
from mainDisplayEngineParameters import *
import threading, os
import time
screen = pygame.display.set_mode((1280, 640))  # dimension of screen

valueTest = 0
stopThreads = False
changePanelVariable = 0

class Game(object):

    def main(self,screen):
        clock = pygame.time.Clock() #take frames

        sprites = pygame.sprite.Group() #add object to a group


        while 1:


            #see event for keyboard
            for e in pygame.event.get():
                global stopThreads
                global changePanelVariable

                if e.type == pygame.QUIT:
                    stopThreads = True
                    changeStopThreads(True)
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    stopThreads = True
                    changeStopThreads(True)
                    return
                #changePanel
                if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
                    IncrementVariablePanel(changePanelVariable)
                    changePanelVariable = changePanelVariable +1





            #set screen and fill background
            screen.fill((0,0,0))
            sprites.draw(screen)
            pygame.display.flip()


            clock.tick(2)





if __name__ == '__main__':
    pygame.init()



    #start thread for display engineParameters
    classEngineParameters = displayEngineParameters()
    classEngineParameters.start()
    ###################################################################


    Game().main(screen)
