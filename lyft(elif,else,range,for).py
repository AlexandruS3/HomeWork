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


DIR_UP           = -1
DIR_STOPPED      = 0
DIR_DOWN         = 1

from os import system

building_roof    = False
building_floors  = 9
building_parking = False

lift_floor       = 4
lift_open        = False
lift_dir         = DIR_UP

humna_floor      = 3
human_in_lift    = True

#################### RENDER FRAME #################### 
system ("cls")


if building_roof:
    print (       "---|-----|----")
    print (       " R |     |    ") 
     
if building_roof == False:
     print (       "---|-----|----")    
for floor in range (9,0,-1):

    
    if floor == lift_floor -1 :

        b = "|---|"
    else:
        b = "     "   


    print (f"---|{b}|----")
    if floor == lift_floor:

        c = "|---|"
    else:
        c = "     "   


    print (f"---|{c}|----")
    
    if floor == humna_floor and not human_in_lift:
        h = " H "
    else:    
        h = "   "

        
    if floor == lift_floor + 1:
        if lift_open:
            l = " < > "
        else:
            if lift_dir == DIR_UP:
                l = "  ^  "
            elif lift_dir == DIR_DOWN:
                l = "  v  " 
            else:
                l = "     "     
    
    else:
        l = "     "



    if floor == lift_floor:
        l = "|   |"
        if human_in_lift == True:
             l = "| H |"
               

    print(f"{floor:^3}|{l}|{h}")

if building_parking  == False:
    print (       "---|-----|----") 

if building_parking:
    print (       "---|     |----") 
    print (       " P |     |    ")
    print (       "---|-----|----") 
#################### RENDER FRAME #################### 