import pygame
from mainDisplayEngineParameters import *
from mainDisplayClockEngine import *
import threading, os
import time
screen = pygame.display.set_mode((1280, 640),16)  # dimension of screen





valueTest = 0
stopThreads = False
changePanelVariable = 0
dirPanel =False
kmhVariableAngle = 0
rpmVariableAngle = 0
angle = 0


class startThreadsClass(threading.Thread):
    def __init__(self):
        super(startThreadsClass, self).__init__()
        threading.Thread.__init__(self)

    def stop(self):
        self._stop()

    def run(self):

        sprites = pygame.sprite.Group()
        self.acrpm = AcKMH(sprites)

        while 1:
            global stopThreads
            if stopThreads == True:
                os._exit(1)

            sprites.draw(screen)

            self.acrpm.update(self.acrpm)
            pygame.display.flip();

            #time.sleep(0.1)

            screen.fill((0, 0, 0),(0,300,400,400))
            print ("ok")




class AcKMH(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcKMH, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(400,400))

        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.center = (200,500)
        self.dir = False

    def update(self,game):
        global angle
        self.angle = angle
        self.image = pygame.transform.rotate(self.originalimage, self.angle)
        if self.dir == False:
            if self.angle < -255:
                self.dir=True
                return
            self.angle -=4
        if self.dir == True:
            if self.angle > 0:
                self.dir = 10
                return
            self.angle +=8

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)


        angle = self.angle
        print (angle)


class Game(object):

    def main(self,screen):
        clock = pygame.time.Clock() #take frames

        while 1:


            #see event for keyboard
            for e in pygame.event.get():
                global stopThreads
                global changePanelVariable
                global dirPanel

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
                    if changePanelVariable == 0:
                        dirPanel = True
                    if changePanelVariable == 2:
                        dirPanel = False
                    IncrementVariablePanel(changePanelVariable)
                    if changePanelVariable <= 2 and dirPanel == False:
                        changePanelVariable = changePanelVariable -1
                    if changePanelVariable >=0 and dirPanel ==True:
                        changePanelVariable = changePanelVariable + 1


            #set screen and fill background
            #screen.fill((0,0,0))
            #screen.fill((0, 0, 0))
            #pygame.display.update()
            pygame.display.flip()


            clock.tick(1)
            #clock.tick(30)
            #time.sleep(0.5)







if __name__ == '__main__':
    pygame.init()



    #####################start thread for display engineParameters#############
    classEngineParameters = displayEngineParameters()
    classEngineParameters.start()
    ###########################################################################

    #####################start thread for display clocks#######################
    classEngineClock=displayMainClock()
    setScreen(screen);
    classEngineClock.start()
    ###########################################################################

    #####start ace thread###########3
    classThreadingthread=startThreadsClass()
    classThreadingthread.start()
    #####################################


    Game().main(screen)
