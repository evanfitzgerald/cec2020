from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile

cube = readfile("easy.txt")
size = 5
storHop = floor(sqrt(size)/2)
drone = Drone(storHop,cube,0,0,size)
print(cube)

#stack sort

#colour sort

#collect all of curColour until full, then place on empty spot. (add to that storage type spot) (xy, xy, ..)
#repeat until curColour is good (outside)
#do for all remaining colours

    if (drone.checkCurColour and not hopper is not full)
        pick up all that colour until full or not cur colour anymore
    elif hopper is full
        go to the current storage space, and drop off as many as possible ,if storage stack fills, find new one and drop off
    else
        move on to next position
        mode type
        if type == 1
            right
            if y = limit
            type = 3
        2
        up
        3
        down
        4
        left

do this for current rim
    then move in rim
    still storing on outside
    until middle...
