from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile
import math

cube = readfile("easy.txt")
sizec = 5**3
size = 5
mode = 1
storHop = int(math.sqrt(sizec)/2)
drone = Drone(storHop,cube,0,0,size)
print(cube)
drone.hop()
x_limit = size-1
y_limit = size-1


def mover(mode, x_limit, y_limit):
    if (mode == 1):
        drone.MoveRight()
        if (drone.x == x_limit):
            mode = 3
    elif (mode == 2):
        drone.MoveLeft()
        if (drone.x == size - (x_limit+1)):
            mode = -1
    elif (mode == 3):
        drone.MoveDown()
        if (drone.y == y_limit):
            mode = 2
    else:
        drone.MoveUp()
        if (drone.y == size - y_limit):
            mode = 1
            y_limit = y_limit - 1
            x_limit = x_limit - 1

    return mode, x_limit, y_limit


for i in range(24):
    mode, x_limit, y_limit = mover(mode, x_limit, y_limit)
    print(drone.x,drone.y)
drone.hop()


print(cube)
