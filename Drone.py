from Block import Block
import Math

class Drone:

    timeComp = 0
    lastTouch = None

    def __init__(self, hopperSize, cube, x, y, z = 0):
        self.hopper = []
        self.hopperSize = hopperSize
        self.x = x
        self.y = y
        self.z = z
        self.cube = cube
        self.timeComp = timeComp
        self.lastTouch = lastTouch

    def MoveUp(self):
        if(self.y == 0):
            print("At top!")
            return
        self.timeComp++;
        self.y -= 1

    def MoveDown(self):
        if(self.y == len(self.cube.scrambled)-1):
            print("At Bottom!")
            return
        self.timeComp++;
        self.y += 1

    def MoveLeft(self):
        if(self.x == 0):
            print("At Left!")
            return
        self.timeComp++;
        self.x -= 1

    def MoveTo(self, x, y):
        if(max(x,y) > self.cube.size or min(x, y) < 0):
            print("Out of bounds")
            return
        dif = (Math.abs(self.x - x) + Math.abs(self.y - y))
        self.timeComp+= dif;
        self.x = x
        self.y = y

    def MoveRight(self):
        if(self.x == len(self.cube.scrambled)-1):
            print("At Right!")
            return
        self.timeComp++;
        self.x += 1

    def hop(self):
        block = None
        z = len(self.cube.scrambled)-1
        while(block == None):
            if (z <= -1):
                return
            block = self.cube.scrambled[self.x][self.y][z]
            z-=1
        if(len(self.hopper) >= self.hopperSize):
            raise IndexError("Hopper is full!")
        if(self.lastTouch == block.colour)
            self.timeComp += 2
        else
            self.timeComp += 3
        self.cube.scrambled[self.x][self.y][z+1] = None
        self.hopper.append(block)
        self.lastTouch = block.colour

    def unhop(self, colour):
        todel = None
        #self.hopper.remove(colour)
        z = self.cube.size-1
        block = None
        while(block == None and z >= -1):
            block = self.cube.scrambled[self.x][self.y][z]
            z -= 1
        if z > self.cube.size-3:
            print("Full!")
            self.hopper.append(Block(colour))
            return
        #print(self.x, self.y,z)
        if(self.lastTouch == block.colour)
            self.timeComp += 2
        else
            self.timeComp += 3
        self.lastTouch = block.colour
        self.cube.scrambled[self.x][self.y][z+2] = Block(colour)
        #print("unhopped", self.cube.scrambled[self.x][self.y][z+2], self.x, self.y, z)

    def HopStack(self, colour = None):
        #self.hop()
        if colour == None:
            colour = self.hopper[-1].colour
        print(colour, len(self.hopper) < self.hopperSize)
        while(len(self.hopper) < self.hopperSize):
            self.hop()
            if self.hopper[-1].colour != colour:
                print("unhopped")
                self.unhop(self.hopper[-1].colour)


    """def unhop(self):
        colour = self.hopper.peek().colour
        todel = None
        self.hopper.remove(colour)
        z = self.cube.size-1
        block = None
        while(block != None):
            block = self.cube.scrambled[self.x][self.y][z]
            z -= 1
        if z ==self.cube.size-2:
            print("Full!")
            return
        self.cube.scrambled[self.x][self.y][z-1] = block
        return colour"""


    def unhopStack(self):
        sortedStack = []
        while(len(self.hopper) > 0):
            lr, lg, lb, lelem, lindex = 0,0,0,None, 0
            for i in range(len(self.hopper)):
                if self.hopper[i].colour[0] > lr:
                    lelem = self.hopper[i]
                    lindex = i
                    lr = self.hopper[i].colour[0]
                if self.hopper[i].colour[0] == lr:
                    if self.hopper[i].colour[1] > lg:
                        lelem = self.hopper[i]
                        lindex = i
                        lg = self.hopper[i].colour[1]

                    if self.hopper[i].colour[1] == lg:
                        if self.hopper[i].colour[2] > lb:
                            lelem = self.hopper[i]
                            lindex = i
                            lb = self.hopper[i].colour[2]
            sortedStack.append(self.hopper.pop(lindex))

        i = 0
        while(len(sortedStack) > i):
            self.unhop(sortedStack[i].colour)
            i+=1

    def printHopper(self):
        for e in hopper:
            print(str(e))

    def __str__(self):
        return str(self.cube) + "\nDrone location: " + str(self.x) + " " + str(self.y)
