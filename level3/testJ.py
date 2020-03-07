from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile
import math
import sys


def mover(mode, x_limit, y_limit, stop, drone, size):
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

def testJ(filename):
    cube = readfile(filename)
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
        mode, x_limit, y_limit, stop = mover(mode, x_limit, y_limit, stop, drone, size)
    stop = 1
    thislistred = []
    drone.MoveTo(0,0)
    gogo = 0
    nota = 0
    superx = 0
    supery = 0
    for i in range(5):
        # if empty
        print("------")

        print(drone.x, drone.y)

        if (cube.colEmpty(drone.x, drone.y, cube.size)): #and ((drone.x,drone.y) not in thislistred)):
            # now we have reds
            print(drone.x)
            print(drone.y)
            print("------")
            print(len(drone.hopper))
            if (len(drone.hopper) > 0):
                drone.unhopStack()
                thislistred.append((drone.x,drone.y))
                superx = drone.x
                supery = drone.y
            mode, x_limit, y_limit, stop = mover(mode, x_limit, y_limit, stop, drone, size)

        else:
            #not empty
            print(1234)
            if(len(drone.hopper) < drone.hopperSize and ((drone.x,drone.y) not in thislistred)):
                print(2222)
                colour = drone.HopStack()
                print(colour)
                drone.printHopper()

            if(len(drone.hopper) == drone.hopperSize):
                mode = 1
                drone.MoveTo(superx,supery)
                x_limit = size-1
                y_limit = size-1

            #check hopper
            # move
            mode, x_limit, y_limit, stop = mover(mode, x_limit, y_limit, stop, drone, size)
    
    return cube
