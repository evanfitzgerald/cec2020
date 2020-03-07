class Cube:

    def __init__(self, scrambled, solved):
        self.scrambled = scrambled
        self.solved = solved
        self.size = len(scrambled)

    def ScanMap(self, x, y):
        for i in range(self.size):
            if(scrambled[x][y][self.size - 1 - i] != None):
                return (self.solved[x][y][size - 1 - i],self.solved[x][y][size - 1 - i])
        
        return (None, None)

    def isEmpty(self, x, y, z):
        return self.scrambled[x][y][z] == None

    def __str__(self):
        stri = ""
        for i in range(self.size):
            for j in range(self.size):

                for k in range(self.size):
                    if(self.scrambled[k][j][i] == None):
                        stri += "WHITE "
                    else:
                        stri += str(self.scrambled[k][j][i]) + " "
                stri += "\n"
            stri += "\n"
        return stri
