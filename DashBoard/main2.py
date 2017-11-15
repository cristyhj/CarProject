import os,pygame


screen = pygame.display.set_mode((500, 500),16)



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
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    return
                #changePanel
                if e.type == pygame.KEYDOWN and e.key == pygame.K_b:
                    print("baga")
                    os.system('python main.py')
                    print("gelu")


            pygame.display.flip()







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
