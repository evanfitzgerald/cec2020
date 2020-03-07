
from Block import Block
from Cube import Cube


def readfile(filename):
    file = open(filename, 'r')
    count = 0
    size = 0
    for line in file.readlines():
        count = count + 1
        if (count == 2):
            size = int(line[5:])
            arr = [[[None for i in range(size)] for j in range(size)] for k in range(size)]
            arr2 = [[[None for i in range(size)] for j in range(size)] for k in range(size)]
        # scrambled
        elif (count > 2 and count > size*size*size+5):
            #print(line)
            l_split = line.split(",")
            rest_split = l_split[2].split("=")
            x = int(l_split[0])
            y = int(l_split[1])
            z = int(rest_split[0])
            if (rest_split[1][1] != "\""):
                arr[x][y][z] = Block(tuple(map(int, rest_split[1][1:-2].split("_"))))
        # unscrambled
        elif (count > 2 and count <= size*size*size+2):
            #print(line)
            l_split = line.split(",")
            rest_split = l_split[2].split("=")
            x = int(l_split[0])
            y = int(l_split[1])
            z = int(rest_split[0])
            if (rest_split[1][1] != "\""):
                arr2[x][y][z] = Block(tuple(map(int, rest_split[1][1:-2].split("_"))))

            
    #print(arr)
    #print("\n")
    #print(arr2)
    c = Cube(arr, arr2)
    return c

if __name__ == "__main__":
    c = readfile("easy.txt")
    print(c.solved)
