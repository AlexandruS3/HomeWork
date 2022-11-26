from os import system
from random import randint
from time import sleep

SCALE  = 10
 # START 
hX = 1   
hY = 1
# FINISH
bx = 4     
by = 8

option = ""

helicop =int(input(
        f"""a. pentru 'ZONA periculoasa' tasteaza: 1
b. pentru 'ZONA cu zgomot' tasteaza: 2
"""
))

while True:

   
    bx = int(input("Helicopter coordinates X "))
    by = int(input("Helicopter coordinates Y "))
    while True:
    ######## RENDER FRAME ###########
        system ("cls")
        map = "" 
        for y in range(SCALE):
            map += str(y) + ". "
            for x in range(SCALE):
                if helicop == 1:
    ######## ZONA PERICULOASA ###########
                    if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
                        map += "# "
                    elif x == hX and y == hY:
                        map += "H "
                    elif x == hX and y == hY - 1:
                        map += "+ "
                    elif x == hX and y == hY + 1:
                        map += "+ "    
                    elif x == hX + 1 and y == hY :
                        map += "+ "        
                    elif x == hX - 1 and y == hY :
                        map += "+ "            
                    elif x == hX - 1 and y == hY - 1:
                        map += "+ "            
                    elif x == hX + 1 and y == hY - 1:
                        map += "+ "
                    elif x == hX + 1 and y == hY + 1:
                        map += "+ "
                    elif x == hX - 1 and y == hY + 1:
                        map += "+ "
                    elif x == hX - 2 and y == hY :
                        map += "+ "
                    elif x == hX + 2 and y == hY :
                        map += "+ "
                    else:
                        map += "  "
    ######## ZONA PERICULOASA ###########
    ######## ZONA CU ZGOMOT ###########            
                else:
                    
                    if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
                        map += "# "
                    elif x == hX and y == hY:
                        map += "H "
                    elif x == hX and y == hY - 1:
                        map += "~ "
                    elif x == hX and y == hY + 1:
                        map += "~ "    
                    elif x == hX + 1 and y == hY :
                        map += "~ "        
                    elif x == hX - 1 and y == hY :
                        map += "~ "            
                    elif x == hX - 1 and y == hY - 1:
                        map += "~ "            
                    elif x == hX + 1 and y == hY - 1:
                        map += "~ "
                    elif x == hX + 1 and y == hY + 1:
                        map += "~ "
                    elif x == hX - 1 and y == hY + 1:
                        map += "~ "
                    elif x == hX - 2 and y == hY :
                        map += "~ "
                    elif x == hX + 2 and y == hY : 
                        map += "~ "
                    elif x == hX - 2 and y == hY -1 :
                        map += "~ "
                    elif x == hX + 2 and y == hY -1 :
                        map += "~ "
                    elif x == hX - 2 and y == hY +1 :
                        map += "~ "
                    elif x == hX + 2 and y == hY +1 :
                        map += "~ "    
                    elif x == hX  and y == hY -2  :
                        map += "~ "    
                    elif x == hX - 1 and y == hY -2  :
                        map += "~ "    
                    elif x == hX + 1 and y == hY -2  :
                        map += "~ "    
                    elif x == hX  and y == hY +2  :
                        map += "~ "    
                    elif x == hX - 1 and y == hY +2  :
                        map += "~ "    
                    elif x == hX + 1 and y == hY +2  :
                        map += "~ "    
                    else:
                        map += "  "

        ######## ZONA CU ZGOMOT ###########        
            map += "\n"                
        
        print(map)
        if hY == by and hX == bx:
            break
            

        ######## RENDER FRAME ###########
        ######### ANIMATION #############
        if hY < by:
            hY += 1
        if hX < bx:
            hX +=1
        if hY > by:
            hY -= 1
        if hX > bx:
            hX -=1
        
       
        ######### ANIMATION #############

        sleep (.5)