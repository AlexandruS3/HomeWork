from os import system
from time import sleep
# LEGEND
# 0 - free
# 1 - reserved
# 2 - bought
seats = [ 0, 0, 1, 2, 0, 0, 0, 0,]
# index   0, 1, 2, 3, 4, 5, 6, 7
option =-1

while option !=0:
    # iterative count algoritm
    free_seats = (len(seats))                           #HW1 let's say free_seats = len(seats)
    for pi in range (len(seats)):
        if seats[pi] == 1 or seats[pi] == 2:
            free_seats -=1
    # ##########################

    # ########## PLOT ##########
    system ("clear")
    print()
    for pi in range (len(seats)):
        print("", pi+1, "", end = "  ")
    print()

    for pi in range (len(seats)):
        if seats[pi] == 1:
            print("|-|", end="  ")
        elif seats[pi] == 2:
            print("|+|", end="  ")
        else:
            print("| |", end="  ")
    print("\nFree seats: ", free_seats)
    print("\n") 
    # ########## PLOT ##########


    # ####### show MENU ########    
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("0. Exit")
    print("--------------------")   
    # ####### show MENU ######## 

    option = int(input(">>> "))
    
    if option == 1:
        place = int(input("Which place? "))
                                                                            #HW2: add check conditions:
        if place <= (len(seats)) and seats[place - 1] not in [1, 2]:        #     - boundaries
           seats[ place -1 ] = 1                                            #     - check if the place is free
        elif seats[place - 1] == 1:
            print("This seat is already booked.")
            sleep(3)
        elif seats[place - 1] == 2:
            print("This seat is already bought.")
            sleep(3)

    if option == 2:
        place = int(input("Which place? "))
        
        if place <= (len(seats)) and seats[place - 1] not in [1, 2]:        #HW3:  
           seats[ place -1 ] = 2                                            #     - add BUY
        elif seats[place - 1] == 1:
            print("This seat is already booked.")
            sleep(3)
        elif seats[place - 1] == 2:
            print("This seat is already bought.")
            sleep(3)        

    if option == 3:
        place = int(input("Which place? "))                                 #     - add CANCEL   
                                                                            #     - check only if BOOKED!!!
        if place <= (len(seats)) and seats[place - 1] not in [0, 2]:
           seats[ place -1 ] = ""
        elif seats[place - 1] == 2:
            print("This seat is bought.")
            sleep(3)
      