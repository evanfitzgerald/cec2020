class Drone:

    def __init__(self, hopperSize, cube, x, y, z = 0):
        self.hopper = []
        self.hopperSize = hopperSize
        self.x = x
        self.y = y
        self.z = z
        self.cube = cube

    def MoveUp(self):
        if(self.y == 0):
            print("At top!")
            return
        self.y -= 1

    def MoveDown(self):
        if(self.y == len(self.cube.scrambled)-1):
            print("At Bottom!")
            return
        self.y += 1

    def MoveLeft(self):
        if(self.x == 0):
            print("At Left!")
            return
        self.x -= 1

    def MoveRight(self):
        if(self.x == len(self.cube.scrambled)-1):
            print("At Right!")
            return
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
        self.cube.scrambled[self.x][self.y][z+1] = None
        self.hopper.append(block)

    def unhop(self, colour):
        todel = None
        self.hopper.remove(colour)
        return colour

    def unhop(self):
        return self.hopper.pop()

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
        return sortedStack

    def printHopper(self):
        for e in hopper:
            print(str(e))

    def __str__(self):
        return str(self.cube) + "\nDrone location: " + str(self.x) + " " + str(self.y)
