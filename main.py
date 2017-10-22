import pygame
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
angleRPM =0
angleKMH = 0
angleTemp = 0
angleFuel = 0
backValuePanelVariable = 0




class AcRPM(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(AcRPM, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.originalimage = pygame.transform.scale(self.originalimage, (400, 400))
        self.rect = pygame.rect.Rect((880, 300), self.originalimage.get_size())
        self.angleRPM = 0

        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage, (400, 400))

        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((880, 300), self.image.get_size())
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.center = (1080, 500)
        self.dir = False





    def update(self,game):
        global angleRPM
        self.image = pygame.transform.rotate(self.originalimage, self.angleRPM)
        if self.dir == False:
            if self.angleRPM < -255:
                self.dir=True
                return
            self.angleRPM -=4
        if self.dir == True:
            if self.angleRPM > 0:
                self.dir = 10
                return
            self.angleRPM +=8

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)

        angleRPM = self.angleRPM
        if angleRPM > -230 and self.dir == False:
            screen.fill((0, 0, 0), (880, 300, 400, 400))
        if self.dir == True or angleRPM == 8:
            screen.fill((0, 0, 0), (880, 300, 400, 400))



class AcTEMP(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcTEMP, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(200,200))

        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())

        self.rect = self.image.get_rect()
        self.rect.center = (1080,460)
        self.dir = False



    def update(self,game):
        global angleTemp

        self.angle = angleTemp


        self.image = pygame.transform.rotate(self.originalimage, self.angle)
        if self.dir == False:
            if self.angle < -255:
                self.dir=True
                return
            self.angle -=2
        if self.dir == True:
            if self.angle > 0:
                self.dir = 10
                return
            self.angle +=4
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)

        if angleTemp < -130:
            self.imagee = pygame.image.load('resources/sensors/tempsenzor1.png')
            self.imagee = pygame.transform.scale(self.imagee, (50, 50))
            self.rectt = pygame.rect.Rect((500, 550), self.imagee.get_size())
            screen.blit(self.imagee, (500, 550))
        else:
            screen.fill((0,0,0),(500,550,50,50))


        angleTemp = self.angle


#################################################################################################
class AcFUEL(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcFUEL, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(200,200))

        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())
        self.rect = self.image.get_rect()
        self.rect.center = (200,460)
        self.dir = False


    def update(self,game):

        global angleFuel
        self.angle = angleFuel
        self.image = pygame.transform.rotate(self.originalimage, self.angle)
        if self.dir == False:
            if self.angle < -255:
                self.dir=True
                return
            self.angle -=2
        if self.dir == True:
            if self.angle > 0:
                self.dir = 10
                return
            self.angle +=4
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)

        if angleFuel > -50:
            ##print sensor if acfuel ########################################################3
            self.imagee = pygame.image.load('resources/sensors/fuelsenzor1.png')
            self.imagee = pygame.transform.scale(self.imagee, (50, 50))
            self.rectt = pygame.rect.Rect((450, 550), self.imagee.get_size())
            screen.blit(self.imagee, (450, 550))
        else:
            screen.fill((0, 0, 0), (450, 550, 50, 50))

        angleFuel = self.angle
################################################################################################


class AcKMH(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcKMH, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(400,400))

        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())
        self.rect = self.image.get_rect()
        self.rect.center = (200,500)
        self.dir = False

        self.angleKMH = 0

    def update(self,game):
        global angleKMH
        self.angleKMH = angleKMH

        self.image = pygame.transform.rotate(self.originalimage, self.angleKMH)
        if self.dir == False:
            if self.angleKMH < -255:
                self.dir=True
                return
            self.angleKMH -=4
        if self.dir == True:
            if self.angleKMH > 0:
                self.dir = 10
                return
            self.angleKMH +=8

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)
        screen.fill((0, 0, 0), (0, 300, 400, 400))


        angleKMH = self.angleKMH
        #print (angleKMH)
###################################################### PRINT  CEAS ###################################




class CeasKMH(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(CeasKMH,self).__init__(*groups)
        self.image = pygame.image.load('resources/kmh.png')
        self.image = pygame.transform.scale(self.image,(400,400))
        self.rect = pygame.rect.Rect((0,300),self.image.get_size())


class CeasRPM(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(CeasRPM, self).__init__(*groups)
        self.image = pygame.image.load('resources/rpmm.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((880, 300), self.image.get_size())


class FuelCeas(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(FuelCeas, self).__init__(*groups)
        self.image = pygame.image.load('resources/fuel.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((100, 360), self.image.get_size())
        self.angle = 0



class TempCeas(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(TempCeas, self).__init__(*groups)
        self.image = pygame.image.load('resources/temp.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((980, 360), self.image.get_size())
        self.angle = 0
#######################################################################################


class displayEngineParameters():
    def __init__(self):
        #super(displayEngineParameters, self).__init__(*groups)
        global valueTest
        self.valueTest = valueTest
        self.myfont = pygame.font.SysFont("monospace", 15)

        self.textEngineRPM = "Engine RPM: " + str(self.valueTest) + " rpm"
        self.textVehicleSpeed = "Speed: " + str(self.valueTest) + "km/h"
        self.textIntakeAirTemp = "Intake Air Temperature: " + str(self.valueTest) + "°"
        self.textThrottlePos = "Throttle: " + str(self.valueTest) + "%"
        self.textIntakeManifoldAbsoluteressure = "Intake manifold pressure: " + str(self.valueTest) + "kPa"
        self.textOilTemp = "Engine Oil Temp: " + str(self.valueTest) + "°"
        self.textEngineCoolantTemp = "Engine Coolant Temp: " + str(self.valueTest) + "°"
        self.textEngineTorque = "Torque: " + str(self.valueTest) + "N/m"
        self.textTurbochargerPressure = "Turbocharger pressure: " + str(self.valueTest) + "kPa"
        self.textFuelTemp = "Fuel Temp: " + str(self.valueTest) + "°"
        self.textDateAndTime = "xx:xx:xx yy/yy/yy"
        self.textConsumption = "Consumption: " + "l/100km"
        self.textRange = "Range:  km"





    def update(self):

        #clock = pygame.time.Clock()

        print (changePanelVariable)
        #global changePanelVariable


        #print(str(changePanelVariable))
        time.sleep(0.05)

        global backValuePanelVariable
        if backValuePanelVariable != changePanelVariable:
            screen.fill((0, 0, 0), (510, 110, 310, 360))
            backValuePanelVariable = changePanelVariable

        if changePanelVariable == 0:
            label1 = self.myfont.render(str(self.textConsumption), 1, (255,50,0))
            screen.blit(label1, (550, 190))

            label1 = self.myfont.render(str(self.textRange), 1, (255, 50, 0))
            screen.blit(label1, (550, 240))

        if changePanelVariable == 1:
            #first table info
            label1 = self.myfont.render(str(self.textEngineRPM), 1, (255,50,0))
            screen.blit(label1, (510, 110))

            label2 = self.myfont.render(str(self.textVehicleSpeed), 1, (255,50,0))
            screen.blit(label2, (510, 150))

            label3 = self.myfont.render(str(self.textEngineCoolantTemp), 1, (255,50,0))
            screen.blit(label3, (510, 190))

            label4 = self.myfont.render(str(self.textFuelTemp), 1, (255,50,0))
            screen.blit(label4, (510, 230))

            label5 = self.myfont.render(str(self.textOilTemp), 1, (255,50,0))
            screen.blit(label5, (510, 270))

            ###########################################################################################################
            # second table info
        if changePanelVariable == 2:
            label6 = self.myfont.render(str(self.textThrottlePos), 1, (255,50,0))
            screen.blit(label6, (510, 110))

            label7 = self.myfont.render(str(self.textIntakeAirTemp), 1, (255,50,0))
            screen.blit(label7, (510, 150))

            label8 = self.myfont.render(str(self.textIntakeManifoldAbsoluteressure), 1, (255,50,0))
            screen.blit(label8, (510, 190))

            label9 = self.myfont.render(str(self.textEngineTorque), 1, (255,50,0))
            screen.blit(label9, (510, 230))

            label10 = self.myfont.render(str(self.textTurbochargerPressure), 1, (255,50,0))
            screen.blit(label10, (510, 270))

        label11 = self.myfont.render(str(self.textDateAndTime), 1, (255,50,0))
        screen.blit(label11, (560, 350))

        pygame.draw.rect(screen, (255,50,0), (500, 100, 300, 350), 2)
        pygame.display.update()


#####################################################################################DISPLAY SENSORS IMAGES#############

class displaySensor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(displaySensor, self).__init__(*groups)
        self.image = pygame.image.load('resources/sensors/fuelsenzor1.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = pygame.rect.Rect((450, 550), self.image.get_size())



    def update(self,game):
        global angleFuel

        if angleFuel > -50:
            screen.fill((255, 0, 0), (450, 550, 50, 50))
            print(angleFuel)



class Game(object):

    def main(self,screen):
        clock = pygame.time.Clock() #take frames

        sprites = pygame.sprite.Group()


        self.ceasKMHImage = CeasKMH(sprites)
        self.ceasRPMImage = CeasRPM(sprites)
        self.ceasTEMPImage = TempCeas(sprites)
        self.ceasFUELImage = FuelCeas(sprites)
        self.displayEnginePar = displayEngineParameters()

        self.acKMH = AcKMH(sprites)
        self.acRPM = AcRPM(sprites)
        self.acTemp = AcTEMP(sprites)
        self.acFuel = AcFUEL(sprites)



        while 1:


            #see event for keyboard
            for e in pygame.event.get():

                global stopThreads
                global changePanelVariable
                global dirPanel

                if e.type == pygame.QUIT:
                    stopThreads = True
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    stopThreads = True
                    return
                #changePanel
                if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
                    if changePanelVariable == 0:
                        dirPanel = True
                    if changePanelVariable == 2:
                        dirPanel = False
                    if changePanelVariable <= 2 and dirPanel == False:
                        changePanelVariable = changePanelVariable -1
                    if changePanelVariable >=0 and dirPanel ==True:
                        changePanelVariable = changePanelVariable + 1



            sprites.draw(screen)

            pygame.display.flip()


            self.displayEnginePar.update()
            self.acKMH.update(self.acKMH)
            self.acRPM.update(self.acRPM)
            self.acTemp.update(self.acTemp)
            self.acFuel.update(self.acFuel)






            clock.tick(30)







if __name__ == '__main__':
    pygame.init()



    #####################start thread for display engineParameters#############
    #classEngineParameters = displayEngineParameters()
    #classEngineParameters.start()
    ###########################################################################

    #####################start thread for display clocks#######################
    #classEngineClock=displayMainClock()
    #classEngineClock.start()
    ###########################################################################

    #####start ace thread###########3
    #classThreadingthread=startThreadsClass()
    #classThreadingthread.start()
    #####################################


    Game().main(screen)
