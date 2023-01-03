# LARGE CODE
# -> functions
# -> modular
from map import *
from ui import *
from time import sleep
while True:     
    clear()
    printMap(gameMap)
  
     
    key = controls()
   

    if key == "x":
        break 
    gameMap[rr][rc] = 0 # erase the robot    
    
    if key == "d" and (rc < 9 and gameMap[rr][rc+1] != 1):              #HW2: add bounadries
        rc +=1 # increment cordonate  
        if ((rc < 9) and (gameMap[rr][rc +1]) == 3) or ((rc < 8) \
            and (gameMap[rr][rc +2]) == 3):                             #HW3: add mines + radar
            danger()
            sleep(2)       

    if key == "a" and (rc > 0 and gameMap[rr][rc-1] != 1):
        rc -=1              # increment cordonate

    
 
    # HW1: add Up/Down moevement
    # HW2: boundaries check right -> 9, left ->0
    # HW3: add some mines, when moving -> radar rc +1, rc +2 note a mine
    #      in case of danger -> WARNING -> danger detected
    if key == "s" and (rr < 9 and gameMap[rr+1][rc] !=1):
        rr +=1                                                           #HW1: add Up/Down
    if key == "w" and (rr > 0 and gameMap[rr-1][rc] !=1):
        rr -=1 

    gameMap[rr][rc] = 2 # put the robot
    