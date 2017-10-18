from main import *
import threading
from main import stopThreads


stopThreads = False
changePanelVariable

def changeStopThreads(newStopThreads):
    global stopThreads
    stopThreads = newStopThreads
    #print(str(stopThreads))

def IncrementVariablePanel(newVariable):
    global changePanelVariable
    changePanelVariable = newVariable +1


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



        while 1:

            global stopThreads
            global changePanelVariable
            print(str(changePanelVariable))

            if stopThreads == True:   #exit from thread
                os._exit(1)

            if changePanelVariable % 2 ==0 :
                #first table info
                label1 = myfont.render(str(textEngineRPM), 1, (255, 255, 0))
                screen.blit(label1, (100, 100))

                label2 = myfont.render(str(textVehicleSpeed), 1, (255, 255, 0))
                screen.blit(label2, (100, 120))

                label3 = myfont.render(str(textEngineCoolantTemp), 1, (255, 255, 0))
                screen.blit(label3, (100, 140))

                label4 = myfont.render(str(textFuelTemp), 1, (255, 255, 0))
                screen.blit(label4, (100, 160))

                label5 = myfont.render(str(textOilTemp), 1, (255, 255, 0))
                screen.blit(label5, (100, 180))

            ###########################################################################################################
            # second table info
            if changePanelVariable % 2 == 1:
                label6 = myfont.render(str(textThrottlePos), 1, (255, 255, 0))
                screen.blit(label6, (100, 100))

                label7 = myfont.render(str(textIntakeAirTemp), 1, (255, 255, 0))
                screen.blit(label7, (100, 120))

                label8 = myfont.render(str(textIntakeManifoldAbsoluteressure), 1, (255, 255, 0))
                screen.blit(label8, (100, 140))

                label9 = myfont.render(str(textEngineTorque), 1, (255, 255, 0))
                screen.blit(label9, (100, 160))

                label10 = myfont.render(str(textTurbochargerPressure), 1, (255, 255, 0))
                screen.blit(label10, (100, 180))

            pygame.display.flip()


            clock.tick(500)
