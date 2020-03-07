class Drone:

    def __init__(self, hopperSize):
        self.hopper = []
        self.hopperSize = hopperSize

    def hop(self, block):
        if(len(self.hopper) >= self.hopperSize):
            raise IndexError("Hopper is full!")
        self.hopper.append(block)

    def unhop(self, colour):
        todel = None
        self.hopper.remove(colour)
        return colour

    def unhop(self):
        return self.hopper.pop()
    
