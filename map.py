# this is MODULE contain the MAP logic
# GAME MAP - matrix
# 0 - empty
# 1 - wall
# 2 - Robot
# 3 - mines
rc = 0
rr = 0
gameMap = [
    [0,0,0,0,0,3,0,0,0,0,], # 0
    [0,3,0,0,0,0,0,0,0,0,], # 1
    [0,0,0,0,1,0,0,0,0,0,],
    [0,0,0,0,1,0,0,0,0,0,],
    [0,0,0,0,1,1,1,0,0,0,],
    [0,0,0,0,1,0,0,0,0,1,],
    [0,0,0,0,0,1,0,0,0,1,],
    [0,0,0,0,0,1,0,0,0,1,],
    [0,0,0,0,0,1,0,0,0,1,],
    [0,0,0,0,0,1,0,0,0,0,], #9
   # 0,1
]


gameMap[rr][rc] = 2 # put the order in the specifice

def p(c):
    print(c + " ", end="")

def printMap(m):
    for ri in range(10):
        for ci in range(10):
            if m[ri][ci] == 0:
                p(".")
            if m[ri][ci] == 1:
                p("#")
            if m[ri][ci] == 2:
                p("R")
            if m[ri][ci] == 3:
                p("M")    
        print()
printMap(gameMap)



        
