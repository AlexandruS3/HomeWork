
rx = 8
ry = 4

for y in range (1,11):

    for x in range (1,11):
        if x == rx and y == ry:
            print ("R", end=" ")
        elif x == rx and y == ry - 1:
            print ("+", end=" ")
        elif x == rx and y == ry + 1:
            print ("+", end=" ")
        
        elif x == rx - 1 and y == ry:
            print ("+", end=" ")
        elif x == rx + 1 and y == ry:
            print ("+", end=" ")   

        elif x == rx - 1 and y == ry - 1:
            print ("+", end=" ")  
        elif x == rx - 1 and y == ry + 1:   
            print ("+", end=" ")      

        elif x == rx + 1 and y == ry - 1:
            print ("+", end=" ")
        elif x == rx + 1 and y == ry + 1:
            print ("+", end=" ")    

        else:
            print(".", end=" ")     
    print()

         