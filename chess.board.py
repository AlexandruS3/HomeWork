## CHESS BOARD + PIECES

# * list 2d / matrix
# * loops and conditionals
# * algoritms

# tuple / constant list
from os import system
from time import sleep
SIZE = (8,8)

EMPTY    = 0
WBKING   = 1
WBQUEEN  = 2
WBBISHOP = 3
WBKNIGHT = 4
WBROOK   = 5 
WBPAWN   = 6

BKING    = 11
BQUEEN   = 12
BBISHOP  = 13
BKNIGHT  = 14
BROOK    = 15 
BPAWN    = 16

# list 2d
board = [
    [  5,  4,  3,  1,  2,  3,  4,  5, ],
    [  6,  6,  6,  6,  6,  6,  6,  6, ],
    [  0,  0,  0,  0,  0,  0,  0,  0, ],
    [  0,  0,  0,  0,  0,  0,  0,  0, ],
    [  0,  0,  0,  0,  0,  0,  0,  0, ],
    [  0,  0,  0,  0,  6,  0,  0,  0, ],
    [  6, 16, 16, 16, 16, 16, 16,  6, ],
    [ 15, 14, 13, 11, 12, 13, 14, 15, ],
    
]

pieces       = " ♚♛♝♞♜♟    ♔♕♗♘♖♙ "
pieces_codes = [" ", "wk", "wq", "wb", "wn", "wr", "wp", " ", " ", " ", " ", "bwk", "bwq", "bwb", "bwn", "bwr", "bwp", " " ]

alphabet = "abcdefgh"
score = 0

game_over = False
while not game_over:
    
    ################################# PRINT BOARD ########################
    system ("cls")
    print("score: ", score )
    print(" ", end="")
   
    for c in alphabet:
        print(f"{c:^5}", end="")

    print()
    for ri in range(SIZE[0] ):
        rc = SIZE[1] - ri
        print(" "+"-----"*SIZE[1])
        print(rc, end="")
        for ci in range(SIZE[1]):
            piece = pieces [ board[ri][ci] ]
            print(f"| {piece}  ", end="")
        print("|")
    print(" "+ "-----"*SIZE[1])
    ################################# PRINT BOARD ########################

    ################################# INTERACTION ########################   
    move = input(" your move > ")         
    what_, from_, to_ = move[0:2], move[2:4], move[4:6]
    if what_ not in pieces_codes or what_ == " ":
        print("The figure you try to move does not exist!")
    else:
        piece_code = pieces_codes.index(what_)
        ri_from      = SIZE[0] - int(from_[1])
        ci_from      = alphabet.index(from_[0])

        ri_to        = SIZE[0] - int(to_[1])
        ci_to        = alphabet.index(to_[0])
        
        if board[ri_from][ci_from] == piece_code:
            if piece_code == WBPAWN:
                if ci_from == ci_to:
                    if ri_to - ri_from == 1 or\
                        ri_to - ri_from == 2 and ri_from == 1:
                        if board[ri_to][ci_to] == EMPTY:
                            board[ri_from][ci_from] = EMPTY
                            board[ri_to][ci_to] = piece_code    
                elif ci_from == ci_to - 1 or ci_from == ci_to +1 :    #HW1 check left / right diagonals
                    if ri_to - ri_from == 1:
                        if board[ri_to][ci_to] != EMPTY:              #HW2 check if there is a piece
                            if board[ri_to][ci_to] == BPAWN:          #HW3 increase the score
                                score +=1
                            if board[ri_to][ci_to] == BKNIGHT:
                                score +=3
                                score +=1
                            if board[ri_to][ci_to] == BBISHOP:
                                score +=3
                            if board[ri_to][ci_to] == BROOK:
                                score +=5  
                            if board[ri_to][ci_to] == BQUEEN:
                                score +=9          
                            board[ri_from][ci_from] = EMPTY
                            board[ri_to][ci_to] = piece_code
                           

                            

        #input()
    ################################# INTERACTION ########################                        