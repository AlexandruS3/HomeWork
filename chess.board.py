## CHESS BOARD + PIECES

# * list 2d / matrix
# * loops and conditionals
# * algoritms

# tuple / constant list
from os import system
SIZE = (8,8)

BKING   = 1
BQUEEN  = 2
BBISHOP = 3
BKNIGHT = 4
BROOK   = 5 
BPAWN   = 6

# list 2d
board = [
    [ 5, 4, 3, 1, 2, 3, 4, 5, ],
    [ 6, 6, 6, 6, 6, 6, 6, 6, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, ],
    
]

alphabet = "abcdefgh"


################################# PRINT BOARD ########################
system ("cls")
# HW1: display horizontal coordinates abcd...
#      using a separate loop here

for i in range(len(alphabet)):
    print("  ", alphabet[i],  end=" ")
print()
for ri in range(SIZE[0] ):
    rc = SIZE[1] - ri
    print(" "+"-----"*SIZE[1])
    print(rc, end="")
    for ci in range(SIZE[1]):
        piece = " "
        if board[ri][ci] == BKING:
            piece = "♔"
        elif board[ri][ci] == BQUEEN:
            piece = "♕" 
        elif board[ri][ci] == BBISHOP:  
            piece = "♗" 
        elif board[ri][ci] == BKNIGHT:  
            piece = "♘" 
        elif board[ri][ci] == BROOK:  
            piece = "♖" 
        elif board[ri][ci] == BPAWN: 
            piece = "♙"                 
        print(f"| {piece}  ", end="")
    print("|")
print(" "+ "-----"*SIZE[1])
################################# PRINT BOARD ########################            