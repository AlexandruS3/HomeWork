# REMAKE 1d robo game.> for loop
from os import system 
roboX  = 5
roboHP = 100
roboBT = 100
LENGTH = 30
heart  = 13
crystal= 16
bombX  = 7
coin   = 9
bombx2 = 2
skull  = -1
option = ""
# game loop
while True :
    
    ################# DRAW MAP    ###################
    system ('cls')
    print ("\n")
    
    for x in range(1, LENGTH  +1): # 1..10
    
        if x == roboX:
            print ("🧛", end=" " )
        elif x == coin:
            print ("🌷", end=" " ) 
        elif x == skull:
            print ("☠", end=" " )         
        elif x == bombX:
            print ("💣", end=" ")
        elif x == heart:
            print ("💖", end=" ")
        elif x == crystal:
            print ("⭐", end=" ")
        elif x == bombx2:
            print ("🚀", end= " ")
        else:
            print (".", end= " ")
    print ("\nHP: ", roboHP)
    print (roboBT, "%")
    print ("\n")
    if roboHP <=10:
            print ("ti se apropie sfirsitul")
    if roboHP <= 1:
    
        print ("you are death")
        break      
    
    ################# DRAW MAP    ###################

    ################# READ INPUT  ###################
    option = input(">>> ")
    ################# READ INPUT  ###################
    #################   DECIDE    ###################
    
    if option == "a" and roboX < LENGTH:
        roboX -= 1
        roboBT -=1

    if option == "d" and roboX < LENGTH:
        roboX += 1 
        roboBT -=1    
    if option == "w" and roboX < LENGTH:
        roboX += 4 
        roboBT -=1    
    # check if bomb
  
    if roboX == bombX  : 
        roboHP -= 10
       
    if roboX == bombx2 :
        roboBT -= 14
    if roboX == crystal :
        roboHP += 5
    if roboX == heart :
        roboHP += 5
    if roboX == coin :
        roboBT += 20
        coin = -1  
        skull = 9  

    if option == "x":
        print ("thanks for playing :)")
        break  
    
    

    #################   DECIDE    ###################


# HW1: sa nu intre in minus
# HW2: second bomb
# HW3: place some hearts -> HP+
# HW4: place some coins -> score
# HW5: add variables-> state of bombs, coins,....amortirea bombei