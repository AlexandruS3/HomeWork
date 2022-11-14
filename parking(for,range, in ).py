PARKING_PLACES = int(input('total locuri de parcere '))
FREE_PLACE = int (input('locul liber '))

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE:
     print("|  |", end="")
    else:
     print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")
