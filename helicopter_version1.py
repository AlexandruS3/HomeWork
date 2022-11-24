from os import system
system ("cls")

SCALE  = 10

hX = 4
hY = 7

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

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

    map += "\n"                

print(map)