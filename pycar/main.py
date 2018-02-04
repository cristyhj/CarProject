#!/usr/bin/python3
# _*_ coding: utf-8 -*_
import pygame
import threading, os
import time
screen = pygame.display.set_mode((1280, 640),16)  # dimension of screen



makebigger = 0

valueTest = 0
stopThreads = False
changePanelVariable = 0
dirPanel =False
kmhVariableAngle = 0
rpmVariableAngle = 0
angle = 0
angleRPM = -120
angleKMH = 0
angleTemp = -40
angleFuel = -40
backValuePanelVariable = 0

voltageBatteryValue = 13.8
checkEngineValue = True
oilPressureValue = True

fuelEficiency = 0

avariiEnable = True
countAvarii = 5


refreshFE = True




class AcRPM(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(AcRPM, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac5test.png')
        self.originalimage = pygame.transform.scale(self.originalimage, (400, 400))
        self.rect = pygame.rect.Rect((880, 300), self.originalimage.get_size())
        self.angleRPM = 0

        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage, (400, 400))

        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((880, 290), self.image.get_size())
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.center = (1080, 490)

        self.dir = False





    def update(self,game):
        global angleRPM
        self.angleRPM = angleRPM
        self.image = pygame.transform.rotate(self.originalimage, self.angleRPM)
        if self.dir == False:
            if self.angleRPM < -250:
                self.dir=True
                return
            self.angleRPM -=6
        if self.dir == True:
            if self.angleRPM > -5:
                self.dir = 10
                return
            self.angleRPM +=12

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (1080, 490)



        angleRPM = self.angleRPM

        screen.fill((0, 0, 0), (880, 290, 400, 400))



class AcFUEL(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcFUEL, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(200,200))

        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())

        self.rect = self.image.get_rect()
        self.rect.center = (1080,500)
        self.dir = False

        self.image = pygame.transform.rotate(self.originalimage, -40)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)


    def update(self,game):
        global angleFuel

        self.angle = angleFuel


        self.image = pygame.transform.rotate(self.originalimage, self.angle)
        if self.dir == False:
            if self.angle < -210:
                self.dir=True
                return
            self.angle -=6
        if self.dir == True:
            if self.angle > -40:
                self.dir = -40
                return
            self.angle +=12
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)


        if angleFuel > -60:
            ##print sensor if acfuel ########################################################3
            self.imagee = pygame.image.load('resources/sensors/fuelsenzor1.png')
            self.imagee = pygame.transform.scale(self.imagee, (50, 50))
            self.rectt = pygame.rect.Rect((450, 550), self.imagee.get_size())
            screen.blit(self.imagee, (450, 550))
        else:
            screen.fill((0, 0, 0), (450, 550, 50, 50))


        angleFuel = self.angle


#################################################################################################
class AcTEMP(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcTEMP, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(200,200))

        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((0, 300), self.image.get_size())
        self.rect = self.image.get_rect()
        self.rect.center = (200,490)
        self.dir = False

        self.image = pygame.transform.rotate(self.originalimage, -40)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)



    def update(self,game):

        global angleTemp
        self.angle = angleTemp
        self.image = pygame.transform.rotate(self.originalimage, self.angle)
        if self.dir == False:
            if self.angle < -210:
                self.dir=True
                return
            self.angle -=6
        if self.dir == True:
            if self.angle > -40:
                self.dir = -40
                return
            self.angle +=12
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)

        if angleTemp < -130:  ###################################################################
            self.imagee = pygame.image.load('resources/sensors/tempsenzor1.png')
            self.imagee = pygame.transform.scale(self.imagee, (50, 50))
            self.rectt = pygame.rect.Rect((500, 550), self.imagee.get_size())
            screen.blit(self.imagee, (500, 550))
        else:
            screen.fill((0, 0, 0), (500, 550, 50, 50))


        angleTemp = self.angle
################################################################################################


class AcKMH(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(AcKMH, self).__init__(*groups)
        self.originalimage = pygame.image.load('resources/ac5test.png')
        self.image = self.originalimage

        self.originalimage = pygame.transform.scale(self.originalimage,(400,400))

        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((0, 290), self.image.get_size())
        self.rect = self.image.get_rect()
        self.rect.center = (200,500)
        self.dir = False

        self.angleKMH = 0

    def update(self,game):
        global angleKMH
        self.angleKMH = angleKMH


        self.image = pygame.transform.rotate(self.originalimage, self.angleKMH)

        if self.dir == False:
            if self.angleKMH < -250:
                self.dir=True
                return
            self.angleKMH -=6
        if self.dir == True:
            if self.angleKMH > -3:
                self.dir = 10
                return
            self.angleKMH +=12

        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (200, 490)################################################3center of images

        screen.fill((0, 0, 0), (0, 290, 400, 400))


        angleKMH = self.angleKMH
        #print (angleKMH)
###################################################### PRINT  CEAS ###################################




class CeasKMH(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(CeasKMH,self).__init__(*groups)
        self.image = pygame.image.load('resources/kmhBunBun1.png')
        self.image = pygame.transform.scale(self.image,(400,400))
        self.rect = pygame.rect.Rect((0,290),self.image.get_size())


class CeasRPM(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(CeasRPM, self).__init__(*groups)
        self.image = pygame.image.load('resources/rpmBunBun1.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = pygame.rect.Rect((880, 290), self.image.get_size())


class FuelCeas(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(FuelCeas, self).__init__(*groups)
        self.image = pygame.image.load('resources/fuel.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((100, 400), self.image.get_size())
        self.angle = 0



class TempCeas(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(TempCeas, self).__init__(*groups)
        self.image = pygame.image.load('resources/temp.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = pygame.rect.Rect((980, 400), self.image.get_size()) ##change ceas position
        self.angle = 0
#######################################################################################


class BarCeas(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(BarCeas, self).__init__(*groups)
        self.image = pygame.image.load('resources/bartest.png')
        self.image = pygame.transform.scale(self.image, (1200, 640))
        self.rect = pygame.rect.Rect((92, 168), self.image.get_size()) ##change ceas position
        self.angle = 0

##########################################################

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
        self.textHorsePower = "Power: "+ str(self.valueTest)+" hp"





    def update(self):

        #clock = pygame.time.Clock()

        #print (changePanelVariable)
        #global changePanelVariable


        #print(str(changePanelVariable))
        time.sleep(0.05)

        global backValuePanelVariable
        if backValuePanelVariable != changePanelVariable:
            screen.fill((0, 0, 0), (510, 400, 310, 120))
            backValuePanelVariable = changePanelVariable

        if changePanelVariable == 0:
            label1 = self.myfont.render(str(self.textConsumption), 1, (255,50,0))
            screen.blit(label1, (550, 400))

            label1 = self.myfont.render(str(self.textRange), 1, (255, 50, 0))
            screen.blit(label1, (550, 440))

        if changePanelVariable == 1:
            #first table info
            label1 = self.myfont.render(str(self.textEngineRPM), 1, (255,50,0))
            screen.blit(label1, (510, 400))

            label2 = self.myfont.render(str(self.textVehicleSpeed), 1, (255,50,0))
            screen.blit(label2, (510, 420))

            label3 = self.myfont.render(str(self.textEngineCoolantTemp), 1, (255,50,0))
            screen.blit(label3, (510, 440))

            label4 = self.myfont.render(str(self.textFuelTemp), 1, (255,50,0))
            screen.blit(label4, (510, 460))

            label5 = self.myfont.render(str(self.textOilTemp), 1, (255,50,0))
            screen.blit(label5, (510, 480))

            ###########################################################################################################
            # second table info
        if changePanelVariable == 2:
            label6 = self.myfont.render(str(self.textThrottlePos), 1, (255,50,0))
            screen.blit(label6, (510, 400))

            label7 = self.myfont.render(str(self.textIntakeAirTemp), 1, (255,50,0))
            screen.blit(label7, (510, 420))

            label8 = self.myfont.render(str(self.textIntakeManifoldAbsoluteressure), 1, (255,50,0))
            screen.blit(label8, (510, 440))

            label9 = self.myfont.render(str(self.textEngineTorque), 1, (255,50,0))
            screen.blit(label9, (510, 460))

            label11 = self.myfont.render(str(self.textHorsePower), 1, (255, 50, 0))
            screen.blit(label11, (510, 480))

            label10 = self.myfont.render(str(self.textTurbochargerPressure), 1, (255,50,0))
            screen.blit(label10, (510, 500))



        label11 = self.myfont.render(str(self.textDateAndTime), 1, (255,50,0))
        screen.blit(label11, (560, 350))

        #pygame.draw.rect(screen, (255,50,0), (500, 100, 300, 350), 2)
        pygame.display.update()


#####################################################################################DISPLAY SENSORS IMAGES#############

class displaySensor(object):

    def update(self,game):
        global voltageBatteryValue
        global checkEngineValue
        global oilPressureValue
        global avariiEnable
        global countAvarii
                                                            ##############################
        if voltageBatteryValue >= 14:
            screen.fill((0, 0, 0), (550, 550, 50, 50))

        else:
            imageBattery = pygame.image.load('resources/sensors/batterysenzor1.png')
            imageBattery = pygame.transform.scale(imageBattery, (50, 50))
            rect1 = pygame.rect.Rect((550, 550), imageBattery.get_size())
            screen.blit(imageBattery,(550,550))



                                                              ###############################
        if checkEngineValue ==True:
            imageCheckEngine = pygame.image.load('resources/sensors/checkengine.png')
            imageCheckEngine = pygame.transform.scale(imageCheckEngine, (50, 50))
            rect2 = pygame.rect.Rect((600, 550), imageCheckEngine.get_size())
            screen.blit(imageCheckEngine, (600, 550))
        else:
            screen.fill((0, 0, 0), (600, 550, 50, 50))


                                                             ##################################
        if oilPressureValue ==True:
            imageOilPressure = pygame.image.load('resources/sensors/oilsenzor.png')
            imageOilPressure = pygame.transform.scale(imageOilPressure, (50, 50))
            rect3 = pygame.rect.Rect((650, 550), imageOilPressure.get_size())
            screen.blit(imageOilPressure, (650, 550))
        else:
            screen.fill((0, 0, 0), (650, 550, 50, 50))


                                                            ####################################3
        if avariiEnable == True:
            imageToLeft = pygame.image.load('resources/toleft.png')
            imageToLeft = pygame.transform.scale(imageToLeft, (80, 80))
            rect4 = pygame.rect.Rect((350, 300), imageToLeft.get_size())
            screen.blit(imageToLeft, (350, 300))

            imageToRight = pygame.image.load('resources/toright.png')
            imageToRight = pygame.transform.scale(imageToRight, (80, 80))
            rect5 = pygame.rect.Rect((835, 300), imageToRight.get_size())
            screen.blit(imageToRight, (835, 300))

        global angleKMH
        count = 0
        dist = 10
        dist2 = 10


        if angleKMH < -80 and angleKMH > -90:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 5
        if angleKMH < -90 and angleKMH > -120:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 6
        if angleKMH < -120 and angleKMH > -150:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 7
        if angleKMH < -150 and angleKMH > -160:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 8
        if angleKMH < -160 and angleKMH > -180:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 9
        if angleKMH < -180 and angleKMH > -200:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 10
        if angleKMH < -200 and angleKMH > -210:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 11
        if angleKMH < -210 and angleKMH > -240:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 12
        if angleKMH < -240 and angleKMH > -260:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 13
        if angleKMH > 0 and angleKMH > -30:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 1
        if angleKMH < -30 and angleKMH > -60:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 2
        if angleKMH < -60 and angleKMH > -70:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 3
        if angleKMH < -70 and angleKMH > -80:
            screen.fill((0, 0, 0), (400, 410, 50, 200))
            count = 4

        while count >=0:
            if count >= 9:
                imageUpKMH = pygame.image.load('resources/up3.png')
                imageUpKMH = pygame.transform.scale(imageUpKMH, (50, 50))
                rect5 = pygame.rect.Rect((400, 472), imageUpKMH.get_size())
                screen.blit(imageUpKMH, (400, 472 - dist2))
                dist2 = dist2 + 12
            else:
                imageUpKMH = pygame.image.load('resources/up4.png')
                imageUpKMH = pygame.transform.scale(imageUpKMH, (50, 50))
                rect5 = pygame.rect.Rect((400, 580), imageUpKMH.get_size())
                screen.blit(imageUpKMH, (400, 580 - dist))
                dist = dist + 12

            count = count -1


        global angleRPM
        count = 0
        dist = 10
        dist2 = 10

        if angleRPM > 0 and angleRPM > -30:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 1
        if angleRPM < -30 and angleRPM > -60:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 2
        if angleRPM < -60 and angleRPM > -70:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 3
        if angleRPM < -70 and angleRPM > -80:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 4
        if angleRPM < -80 and angleRPM > -90:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 5
        if angleRPM < -90 and angleRPM > -120:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 6
        if angleRPM < -120 and angleRPM > -150:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 7
        if angleRPM < -150 and angleRPM > -160:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 8
        if angleRPM < -160 and angleRPM > -180:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 9
        if angleRPM < -180 and angleRPM > -200:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 10
        if angleRPM < -200 and angleRPM > -210:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 11
        if angleRPM < -210 and angleRPM > -240:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 12
        if angleRPM < -240 and angleRPM > -260:
            screen.fill((0, 0, 0), (830, 410, 50, 200))
            count = 13


        while count >=0:
            if count >= 9:
                imageUpKMH = pygame.image.load('resources/up3.png')
                imageUpKMH = pygame.transform.scale(imageUpKMH, (50, 50))
                rect5 = pygame.rect.Rect((830, 472), imageUpKMH.get_size())
                screen.blit(imageUpKMH, (830, 472 - dist2))
                dist2 = dist2 + 12
            else:
                imageUpKMH = pygame.image.load('resources/up4.png')
                imageUpKMH = pygame.transform.scale(imageUpKMH, (50, 50))
                rect5 = pygame.rect.Rect((830, 580), imageUpKMH.get_size())
                screen.blit(imageUpKMH, (830, 580 - dist))
                dist = dist + 12

            count = count -1

        global fuelEficiency
        count = 0
        dist1 = 0
        dist2 = 0


        if fuelEficiency >6:
           screen.fill((0, 0, 0), (500, 300, 300, 50))
           count = 10
           while count > 0:
                imageUpFE = pygame.image.load('resources/fe3.png')
                imageUpFE = pygame.transform.scale(imageUpFE, (50, 50))
                rect7 = pygame.rect.Rect((620, 300), imageUpFE.get_size())
                screen.blit(imageUpFE, (620+dist1, 300))


                imageUpFE2 = pygame.image.load('resources/fe3.png')
                imageUpFE2 = pygame.transform.scale(imageUpFE2, (50, 50))
                rect8 = pygame.rect.Rect((620, 300), imageUpFE2.get_size())
                screen.blit(imageUpFE2, (620 - dist1, 300))

                dist1 = dist1 + 12
                count = count - 1

        if fuelEficiency <6 and fuelEficiency >=5:
            count = 8
            dist1 = 0
            screen.fill((0, 0, 0), (500, 300, 300, 50))
            while count > 0:
                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 + dist1, 300))

                dist1 = dist1 + 12
                count = count - 1


        if fuelEficiency >=4 and fuelEficiency <= 5:
            count = 4
            dist2 = 0
            dist1 = 0
            screen.fill((0, 0, 0), (500, 300, 300, 50))
            while count > 0:
                imageUpFE3 = pygame.image.load('resources/fe3.png')
                imageUpFE3 = pygame.transform.scale(imageUpFE3, (50, 50))
                rect9 = pygame.rect.Rect((620, 300), imageUpFE3.get_size())
                screen.blit(imageUpFE3, (620 + dist1, 300))


                imageUpFE4 = pygame.image.load('resources/fe3.png')
                imageUpFE4 = pygame.transform.scale(imageUpFE4, (50, 50))
                rect10 = pygame.rect.Rect((620, 300), imageUpFE4.get_size())
                screen.blit(imageUpFE4, (620 - dist1, 300))

                dist1 = dist1 + 12
                count = count -1

            count2 = 1
            while count2 >=0:
                imageUpFE5 = pygame.image.load('resources/fe2.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))


                imageUpFE6 = pygame.image.load('resources/fe2.png')
                imageUpFE6 = pygame.transform.scale(imageUpFE6, (50, 50))
                rect12 = pygame.rect.Rect((620, 300), imageUpFE6.get_size())
                screen.blit(imageUpFE6, (620 + dist1, 300))

                dist1 = dist1 + 12
                count2 = count2 -1




        if fuelEficiency <4 and fuelEficiency >=3:
            count = 2
            dist1 = 0
            screen.fill((0, 0, 0), (500, 300, 300, 50))
            while count >0:
                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 + dist1, 300))

                dist1 = dist1 +12
                count = count -1
            count2 = 3
            while count2 >0:
                imageUpFE5 = pygame.image.load('resources/fe2.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE6 = pygame.image.load('resources/fe2.png')
                imageUpFE6 = pygame.transform.scale(imageUpFE6, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE6.get_size())
                screen.blit(imageUpFE6, (620 + dist1, 300))

                dist1 = dist1 + 12
                count2 = count2 -1


        if fuelEficiency <3 and fuelEficiency >=2:
            count = 1
            dist1 = 0
            screen.fill((0, 0, 0), (500, 300, 300, 50))
            while count > 0:
                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 + dist1, 300))

                dist1 = dist1 + 12
                count = count - 1
            count2 = 4
            while count2 > 0:
                imageUpFE5 = pygame.image.load('resources/fe2.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE6 = pygame.image.load('resources/fe2.png')
                imageUpFE6 = pygame.transform.scale(imageUpFE6, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE6.get_size())
                screen.blit(imageUpFE6, (620 + dist1, 300))

                dist1 = dist1 + 12
                count2 = count2 - 1
        if fuelEficiency < 2 and fuelEficiency >= 1:
            count = 1
            dist1 = 0
            screen.fill((0, 0, 0), (500, 300, 300, 50))
            while count > 0:
                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE5 = pygame.image.load('resources/fe3.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 + dist1, 300))

                dist1 = dist1 + 12
                count = count - 1
            count2 = 7
            while count2 > 0:
                imageUpFE5 = pygame.image.load('resources/fe2.png')
                imageUpFE5 = pygame.transform.scale(imageUpFE5, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE5.get_size())
                screen.blit(imageUpFE5, (620 - dist1, 300))

                imageUpFE6 = pygame.image.load('resources/fe2.png')
                imageUpFE6 = pygame.transform.scale(imageUpFE6, (50, 50))
                rect11 = pygame.rect.Rect((620, 300), imageUpFE6.get_size())
                screen.blit(imageUpFE6, (620 + dist1, 300))

                dist1 = dist1 + 12
                count2 = count2 - 1


class Game(object):

    def main(self,screen):
        clock = pygame.time.Clock() #take frames

        sprites = pygame.sprite.Group()


        self.ceasKMHImage = CeasKMH(sprites)
        self.ceasRPMImage = CeasRPM(sprites)
        #self.ceasTEMPImage = TempCeas(sprites)
        #self.ceasFUELImage = FuelCeas(sprites)
        self.displayEnginePar = displayEngineParameters()

        self.barceas = BarCeas(sprites)


        self.acTemp = AcTEMP(sprites)
        self.acFuel = AcFUEL(sprites)
        self.acKMH = AcKMH(sprites)
        self.acRPM = AcRPM(sprites)

        self.dispSensors = displaySensor()


        while 1:


            #see event for keyboard
            for e in pygame.event.get():

                global stopThreads
                global changePanelVariable
                global dirPanel

                if e.type == pygame.QUIT:
                    stopThreads = True
                    exit(1)
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    stopThreads = True
                    exit(1)
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
            self.acTemp.update(self.acTemp)
            self.acFuel.update(self.acFuel)
            self.acKMH.update(self.acKMH)
            self.acRPM.update(self.acRPM)


            self.dispSensors.update(self.dispSensors)

            global fuelEficiency
            global refreshFE
            if refreshFE == True:
                fuelEficiency = fuelEficiency + 0.5


            if fuelEficiency > 9:
                refreshFE = False

            if refreshFE == False:
                fuelEficiency = fuelEficiency - 0.5

            if fuelEficiency == 1.5 and refreshFE == False:
                refreshFE = -1


            clock.tick(30)







if __name__ == '__main__':
    pygame.init()



    Game().main(screen)
