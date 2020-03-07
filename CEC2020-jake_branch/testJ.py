from Block import Block
from Cube import Cube
from Drone import Drone
from readfile import readfile
import math

cube = readfile("easy.txt")
size = 5**3
storHop = int(math.sqrt(size)/2)
drone = Drone(storHop,cube,0,0,size)
print(cube)
drone.hop()
drone.hop()

print(cube)
