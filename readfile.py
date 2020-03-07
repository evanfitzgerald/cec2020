
def readfile(filename):
    file = open(filename, 'r')
    count = 0
    size = 0
    for line in file.readlines():
        count = count + 1
        if (count == 2):
            size = int(line[5])
            arr = [[[0 for i in range(size)] for j in range(size)] for j in range(size)]
            arr2 = [[[0 for i in range(size)] for j in range(size)] for j in range(size)]
        # scrambled
        elif (count > 2 and count > size*size*size+5):
            #print(line)
            x = int(line[0])
            y = int(line[2])
            z = int(line[4])
            if (line[7] != "\""):
                arr[x][y][z] = tuple(line[7:-2].split("_"))
        # unscrambled
        elif (count > 2 and count <= size*size*size+2):
            print(line)
            x = int(line[0])
            y = int(line[2])
            z = int(line[4])
            if (line[7] != "\""):
                arr2[x][y][z] = tuple(line[7:-2].split("_"))
    print(arr)
    print("\n")
    print(arr2)

readfile("easy.txt")
