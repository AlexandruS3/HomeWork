
from os import system
from time import sleep
from random import randint
# robot cords
rx = 5
# bullet coords / -1 - not active
bx = -1
by = -1
# target cordinates
tx = 5 
ty = 3 

# score
score = 0

option = ""

while option != "x":
    ############## DRAW THE MAP ##############
    system ("cls")
    for y in range (1,11):
        for x in range (1,11):
            if x == rx and y == 10:
                print ("R", end =" ")
            elif x == bx and y == by:
                print ("^", end =" ")
            elif x == tx and y == ty:
                print ("X", end =" ")    
            else:
                print (".", end= " ")    
        print ()
    print ("\nSCORE: ", score)
    ############## DRAW THE MAP ##############
    ##############    BULET     ############## 
    
    if by != -1:
        by -= 1
        if bx == tx and by == ty:   
            ty = randint (1,7) 
            tx = randint (1,10)
            by = -1 
            score += 10
            
        continue

    ##############    BULET     ############## 
    ##############    CONTROL   ##############  
    option = input (">>> ")
    if option == "d":
        rx +=1
    if option == "a":
        rx -=1
    if option == " ":
        bx = rx
        by = 10 - 6
    ##############    CONTROL   ##############    
  