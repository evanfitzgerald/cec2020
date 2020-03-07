class Drone:

    def __init__(self, hopperSize, cube, x, y, z = 0):
        self.hopper = []
        self.hopperSize = hopperSize
        self.x = x
        self.y = y
        self.z = z
        self.cube = cube

    def hop(self):
        block = None
        z = 0
        while(block == None):
            block = self.cube[x][y][z]
            z+=1
        if(len(self.hopper) >= self.hopperSize):
            raise IndexError("Hopper is full!")
        self.cube[x][y][z-1] = None
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
