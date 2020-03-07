from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile
import math

cube = readfile("easy.txt")
size = cube.size
sizec = size**3
mode = 1
stop = 0
storHop = int(math.sqrt(sizec)/2)
drone = Drone(storHop,cube,0,0,size)
print(cube)
drone.hop()
x_limit = size-1
y_limit = size-1


def mover(mode, x_limit, y_limit, stop):
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
            stop = 1

    return mode, x_limit, y_limit, stop
'''
print(drone.x)
print(drone.y)
print(cube.colEmpty(drone.x, drone.y, cube.size))
mode, x_limit, y_limit = mover(mode, x_limit, y_limit)
print(drone.x)
print(drone.y)
print(cube.colEmpty(drone.x, drone.y, cube.size))
for i in range(15):
    mode, x_limit, y_limit = mover(mode, x_limit, y_limit)
print(drone.x)
print(drone.y)
print(cube.colEmpty(drone.x, drone.y, cube.size))
'''
# first part to sort each stack before we start moving
count = 0
while (stop == 0):
    print(count)
    drone.hop()
    drone.hop()
    drone.hop()
    drone.hop()
    drone.hop()
    drone.unhopStack()
    mode, x_limit, y_limit, stop = mover(mode, x_limit, y_limit, stop)
stop = 1

colour = "RED"
drone.MoveTo(0,0)
while True:
    # if empty
    print("->", cube.colEmpty(drone.x, drone.y, cube.size))
    if (cube.colEmpty(drone.x, drone.y, cube.size)):
        if(len(drone.hopper) < drone.hopperSize):
            drone.HopStack((255,0,0))
        #check hopper
        # move
        mode, x_limit, y_limit, stop = mover(mode, x_limit, y_limit, stop)
    else:
        drone.hop()
    break
print(cube)
