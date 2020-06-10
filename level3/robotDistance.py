# Basically it is a game where the user can enter either of the steps - "UP", "DOWN", "LEFT","RIGHT" and the number  continuously
# UP 3
# LEFT 2
# STOP 0
# you calculate the distance travelled from the center and print it
import math
pos = [0,0] # one for x axis and another for y axis movement
while 1:
    (step, distance) =  input("Enter direction & number of steps ").split()
    if step == "STOP" and distance == 0:
        break
    distance = int(distance)
    if step == "LEFT":
        pos[0] -= distance
    elif step == "RIGHT":
        pos[0] += distance   
    elif step == "UP":
        pos[1] += distance   
    elif step == "DOWN":
        pos[1] -= distance    
    else:
        pass
print(int(round(math.sqrt(pos[0]**2 + pos[1] ** 2))))