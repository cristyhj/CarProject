from main import *
import threading
from main import stopThreads
from tkinter import *

stopThreads = False
changePanelVariable

def changeStopThreads(newStopThreads):
    global stopThreads
    stopThreads = newStopThreads
    #print(str(stopThreads))

def IncrementVariablePanel(newVariable):
    global changePanelVariable
    changePanelVariable = newVariable


class displayEngineParameters(threading.Thread):
    def __init__(self):
        super(displayEngineParameters,self).__init__()
        threading.Thread.__init__(self)
        global valueTest
        self.valueTest = valueTest


    def stop(self):
        self._stop()

    def run(self):
        clock = pygame.time.Clock()
        myfont = pygame.font.SysFont("monospace", 15)

        textEngineRPM = "Engine RPM: " + str(self.valueTest) + " rpm"
        textVehicleSpeed = "Speed: " + str(self.valueTest) + "km/h"
        textIntakeAirTemp = "Intake Air Temperature: " + str(self.valueTest) + "°"
        textThrottlePos = "Throttle: " + str(self.valueTest) + "%"
        textIntakeManifoldAbsoluteressure = "Intake manifold pressure: " + str(self.valueTest) + "kPa"
        textOilTemp = "Engine Oil Temp: " + str(self.valueTest) + "°"
        textEngineCoolantTemp = "Engine Coolant Temp: " + str(self.valueTest) + "°"
        textEngineTorque = "Torque: " + str(self.valueTest) + "N/m"
        textTurbochargerPressure = "Turbocharger pressure: " + str(self.valueTest) + "kPa"
        textFuelTemp = "Fuel Temp: " + str(self.valueTest) + "°"
        textDateAndTime="xx:xx:xx yy/yy/yy"
        textConsumption="Consumption: " + "l/100km"
        textRange="Range:  km"



        while 1:

            global stopThreads
            global changePanelVariable
            #print(str(changePanelVariable))
            time.sleep(0.05)


            if stopThreads == True:   #exit from thread
                os._exit(1)

            if changePanelVariable == 0:
                label1 = myfont.render(str(textConsumption), 1, (255,50,0))
                screen.blit(label1, (550, 190))

                label1 = myfont.render(str(textRange), 1, (255, 50, 0))
                screen.blit(label1, (550, 240))

            if changePanelVariable == 1:
                #first table info
                label1 = myfont.render(str(textEngineRPM), 1, (255,50,0))
                screen.blit(label1, (510, 110))

                label2 = myfont.render(str(textVehicleSpeed), 1, (255,50,0))
                screen.blit(label2, (510, 150))

                label3 = myfont.render(str(textEngineCoolantTemp), 1, (255,50,0))
                screen.blit(label3, (510, 190))

                label4 = myfont.render(str(textFuelTemp), 1, (255,50,0))
                screen.blit(label4, (510, 230))

                label5 = myfont.render(str(textOilTemp), 1, (255,50,0))
                screen.blit(label5, (510, 270))

            ###########################################################################################################
            # second table info
            if changePanelVariable == 2:
                label6 = myfont.render(str(textThrottlePos), 1, (255,50,0))
                screen.blit(label6, (510, 110))

                label7 = myfont.render(str(textIntakeAirTemp), 1, (255,50,0))
                screen.blit(label7, (510, 150))

                label8 = myfont.render(str(textIntakeManifoldAbsoluteressure), 1, (255,50,0))
                screen.blit(label8, (510, 190))

                label9 = myfont.render(str(textEngineTorque), 1, (255,50,0))
                screen.blit(label9, (510, 230))

                label10 = myfont.render(str(textTurbochargerPressure), 1, (255,50,0))
                screen.blit(label10, (510, 270))

            label11 = myfont.render(str(textDateAndTime), 1, (255,50,0))
            screen.blit(label11, (560, 350))

            pygame.draw.rect(screen, (255,50,0), (500, 100, 300, 350), 2)
            pygame.display.update()

            time.sleep(1)

            screen.fill((0,0,0),(510,110,310,360))


            #pygame.display.flip()
            clock.tick(60)
