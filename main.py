import sys, pygame, random, time
import world,colors                                 # continent stuff
from pygame.locals import *    

def main():   
    pygame.init()

    # World info---------------------------------------------------------
    gSize = 8                                                       # size of each square
    wdt = 100                                                       # width
    hgt = 75                                                        # height
    size = width, height = gSize*wdt, gSize*hgt                     # screen sizes

    screen = pygame.display.set_mode(size)                          # create a screen
    
    mainWorld = world.World()
    mainWorld.MakeGrid(wdt,hgt)                                     # make list of grid places
    grid_free = []
    grid_free = mainWorld.worldgrid.copy()                          # make copy of the list to use in continent areas

    con1 = world.Continent("A",colors.blue,wdt,hgt,grid_free)       # ------------------
    con2 = world.Continent("B",colors.red,wdt,hgt,grid_free)        # create continents
    con3 = world.Continent("C",colors.green,wdt,hgt,grid_free)      # 
    con4 = world.Continent("D",colors.white,wdt,hgt,grid_free)      #
    con5 = world.Continent("E",colors.gray,wdt,hgt,grid_free)       #
                                                                    #
    con6 = world.Continent("F",colors.yellow,wdt,hgt,grid_free)     #
    con7 = world.Continent("G",colors.pink,wdt,hgt,grid_free)       #
    con8 = world.Continent("H",colors.purple,wdt,hgt,grid_free)     #
    con9 = world.Continent("I",colors.d_red,wdt,hgt,grid_free)      #
    con0 = world.Continent("J",colors.d_blue,wdt,hgt,grid_free)     # ------------------
    
    c_list = [con0,con1,con2,con3,con4,con5,con6,con7,con8,con9]

    for x in range(0,100):                      #cover the screen with continents
        for x in c_list:
            x.spread()
        if not grid_free:
            break
    mainWorld.Waterlevels(c_list)               # set waterlevels
    for x in c_list:
        x.drawSelf(screen)                      # draw the coordinates
        
    pygame.display.update()                     # update screen
  
    while True:    
        for event in pygame.event.get():            # --------------------------
            if event.type == pygame.QUIT:           # close down without a fight
                pygame.display.quit()               #
                sys.exit()                          # ---------------------------
        

main()
     
 
 
