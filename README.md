# CEC2020 - Programming Competition
## Team Nueltin

# Problem Statement

You work for an engineering company that specializes in creating art by 3D printing
images and models. Clients come to you with an image in mind, and your company
helps them make it a reality. The way that your product works is by individually
printing 3D ‘pixels’, and gluing them into their proper places. Once the model is
complete, it is shipped to your clients as one big piece. Unfortunately, the glue that
was used for your last shipment of models was not strong enough and has left several
clients with scrambled models, with all the pixels in the wrong location!

Luckily, your boss has been able to get his hands on some drones that will be able to
help apply glue back to the 3D pixels. Instead of travelling to the client headquarters
and rearranging the blocks yourself, these drones Will be deployed to all the clients as
required. As these drones must be capable of visiting multiple clients, they must be
able to unscrarnble multiple different models

Your team has been tasked to write the control software for the drone. This includes
the software to pickup, drop off, scan a location, etc. Your team is also responsible for
creating an algorithm that will unscramble the models as efficiently as possible. Your
boss will provide you with the size, unscrambled block locations, and scrambled block
locations for each model.

# The Solution

Each section of the solution is placed in separate directories, as per the competition guidelines. The sections are:
### Level 1A: Drone Backend
- Storage hopper for the drone
- Functions to move in the +/— x and y directions. Within this create the ability for the drone to automatically move to the highest 2 location of a given (x, y) location
- Functions to pick up, drop off, and scan the location that your drone is currently at (restrictions on this can be found in the “Rules"

### Level 1B: System Backend
- Read in and store both the scrambled anol unscrarnbled image
- Keep track of locations that have been checked, blocks that have been moved, or any other information that might be valuable to the algorithm
- Create a system to track the time that will keep track of the time required for each move that your drone is doing (more info in “Additional Information")

### Level 2: Algorithm
- Create the algorithm, using your drone’s control software, to unscrarnble the scrambled model
- Once the drone has read in the scrambled and unscrambled models, the program should run autonomously without user interaction
- Output the final information after it is done running (ie time taken, original image, the now unscrambled image, and any other info you think might be useful)

### Level 3: Visualization
- Create a visualization to show the image being unscrambled
- Note: You can still earn points for providing documentation about how you would implement this level of the program, without actually implementing it

# Running the program
- You will require python3 to run the solution
- Run the command `python3 testJ.py <filename>` to execute the solution for any given input data
- For Level 3, additional instructions are given in level 3's readme
