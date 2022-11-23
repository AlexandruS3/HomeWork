
# LIFT SIMULATION / realms situation

# * conditionals / looping / branching
# * logic wrapping / inside-out
# * logical sequences / conections

# ---|-----|----
#  R |     |
# ---|-----|----
#  9 |     |
# ---|-----|----
#  8 |     |
# ---|-----|----
#  7 |     |
# ---|-----|----
#  6 |     |
# ---|-----|----
#  5 |     |
# ---|-----|----
#  4 |  ^  |
# ---||---||----
#  3 ||   || H
# ---||---||----
#  2 |     |
# ---|-----|----
#  1 |     |
# ---|-----|----
#  P |     |
# ---|-----|----

######### SOLUTIONS #########

# * focus / centric

# * enviroment / input
# * language
# * output / template


DIR_UP           = -1
DIR_STOPPED      = 0
DIR_DOWN         = 1

from os import system
from time import sleep

building_roof     = True
building_floors   = 4
building_parking  = True

lift_floor        = 4
lift_open         = False
lift_dir          = DIR_UP
lift_target_floor = 9

humna_floor       = 3
human_in_lift     = True

#################### RENDER FRAME #################### 
system ("cls")
while True:
    humna_floor  = int(input("Where is the human? "))
    human_in_lift = input("Is human inside lift (y/n?") == "y"
    call_lift = input ("Call the lift (y/n? ") == "y"

    if call_lift :
        if not human_in_lift:
            lift_target_floor = humna_floor
        else:
            lift_target_floor = int(input("Where to go? "))

    lift_open = True
    if lift_floor < lift_target_floor:
        speed = +1
        lift_dir = DIR_UP
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = DIR_DOWN
    if lift_floor == lift_target_floor:
        speed = 0        
           
    ##### ANIMATION #########
    while True:
        
        lift_floor += speed

        if lift_floor == lift_target_floor:
            lift_open = True
            lift_dir  = DIR_STOPPED

        #################### RENDER FRAME ####################
        system ("cls")
        
        a = "     "
         
        if building_roof:
            if lift_target_floor == lift_floor == 9:
                a  = " < > "   


            print (       "---|-----|----")
            print (      f" R |{a}|   ") 

    
        for floor in range (9,0,-1) :
               
            a = "     "
            c = "     "
            t = "     "
            s = "     "
           
        
            
            if floor == lift_floor :
                if lift_dir  == DIR_STOPPED :   
                        s = "H"    

    
            
            if floor == lift_floor +1 :
                if lift_dir == DIR_DOWN:
                    a = "  v  "
                elif lift_dir == DIR_UP:
                    a = "  ^  "
                elif lift_dir == DIR_STOPPED and lift_open:
                    a  = " < > " 
                elif floor == 9 :
                    a  = " < > "   
               
                    
                    
            elif floor == lift_floor  :
                a = "|   |"
                t = "|---|"
                if human_in_lift:
                    a = "| H |"
                    if lift_dir == DIR_STOPPED:
                        a = "|   |"
                   
                    

               
                    
            elif floor == lift_floor -1:
                t = "|---|"
                
            elif floor == humna_floor:
                
                if not human_in_lift:
                    s = "H"      
               



            print (      f"---|{t}|----")
            print(f"{floor:^3}|{a}|{s}")
        
        if building_parking:
            if lift_target_floor == lift_floor == 1:
                c  = "|---|" 

        if building_parking:
           
            print (      f"---|{c}|----") 
            print (      f" P |     |    ")
            print (       "---|-----|----") 
        #################### RENDER FRAME ####################    

        sleep (1)
        if lift_floor == lift_target_floor:
            break
    ######### ANIMATION #################
    sleep (.5)        



#    | {a} |                floor + 1

#    | {t} | 
# ---| {c} |----
#           {s}             floor
#    | {t} |                floor -1



# ---||---||----
#  3 ||   || H
# ---||---||----
#  2 |     |