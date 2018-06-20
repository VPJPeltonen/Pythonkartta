import pygame, random, time

class Continent:
    def __init__(self, name, color, wdt, hgt, grid_free):
        self.name = name
        self.color = color
        self.grid_free = grid_free
        while True:
            self.X = random.randint(0,wdt)
            self.Y = random.randint(0,hgt)
            if (self.X,self.Y) in self.grid_free:
                break
        self.areas = [(self.X,self.Y)]
        self.done_areas = []
        self.grid_free.remove((self.X,self.Y)) 

    #----draw the continent-----
    def drawSelf(self, screen):
        for x in self.areas:
            pygame.draw.rect(screen, self.color,(x[0]*8,x[1]*8,8,8))
        for x in self.done_areas:
            pygame.draw.rect(screen, self.color,(x[0]*8,x[1]*8,8,8))            

    #----Spread the continents----
    def spread(self):        
        self.temp_areas = self.areas.copy()
        for x in self.temp_areas:
            flip = random.randint(0,1)
            if flip == 1:
                self.done = True
                if (x[0]-1,x[1]) in self.grid_free:     #if left
                    self.areas.append((x[0]-1,x[1]))
                    self.grid_free.remove((x[0]-1,x[1]))
                    self.done = False
                if (x[0],x[1]-1) in self.grid_free:     #if top
                    self.areas.append((x[0],x[1]-1))
                    self.grid_free.remove((x[0],x[1]-1))
                    self.done = False
                if (x[0]+1,x[1]) in self.grid_free:     #if right
                    self.areas.append((x[0]+1,x[1]))
                    self.grid_free.remove((x[0]+1,x[1]))
                    self.done = False
                if (x[0],x[1]+1) in self.grid_free:     #if bottom
                    self.areas.append((x[0],x[1]+1))
                    self.grid_free.remove((x[0],x[1]+1))
                    self.done = False
                if self.done == True:
                    self.done_areas.append(x)
                    self.areas.remove(x)
                
class World:
    def __init__(self):
        self.name = "Default world"
    # world grid--------------------------------------------
    def MakeGrid(self,wdt,hgt):
        self.worldgrid = []
        for x in range(0,wdt):          # check with all squares
            for y in range(0,hgt):
                self.tempX = x               # x coordinate
                self.tempY = y               # y coordinate
                self.worldgrid.append((x,y))
