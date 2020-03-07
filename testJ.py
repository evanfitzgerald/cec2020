from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile
import math

cube = readfile("easy.txt")
size = 5**3
mode = 1
storHop = int(math.sqrt(size)/2)
drone = Drone(storHop,cube,0,0,size)
print(cube)
drone.hop()

if (mode == 1):
    drone.right()
    if (x == x_limit)
        mode = 3
elif (mode == 2):
    drone.left()
elif (mode == 3):
    drone.down()
else:
    dronw.up()
print(cube)
