from os import system
system ("cls")
print ()
m = 13
l = 9

for r in range (m):
    for s in range (l):
        if r == 0 or r == m-1:
            print ("--", end = "")
       
        elif s == 0:
            print ("| ", end = "")
        elif s == l-1:
            print (" |", end = "")
        elif r == m/2 or r == (m-1)/2: 
                  print ("--", end = "")
        elif s == l/2 or s == (l-1)/2:  
            print ("| ", end = "")            
        else:
            print ("  ", end = "")    
    print()         
