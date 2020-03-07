class Block:
    colorDicty = {(255, 0, 0): "RED", (0,255,0): "GREEN", (0,0,255): "BLUE", (255, 165,0) : "ORANGE", (255,255,0): "YELLOW"}
    def __init__(self,colour):
        self.colour = colour

    def __eq__(self, block2):
        if block2 == None:
            return False
        return self.colour == block2.colour

    def __str__(self):
        if(Block.colorDicty.get(self.colour) != None):
            return Block.colorDicty[self.colour]
        return str(self.colour)