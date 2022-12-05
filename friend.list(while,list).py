# FACT: list of friends



# empty list
from os import system
system ("cls")
friends = []

while len ( friends ) < 100:
    name = input (" Add friend name: ")
    if name == "":
        
        break
    if name in friends:
     friends.remove (name)

    friends.append( name ) 
    
        

        

print("You have", len( friends ), "frineds" )
for i in range( len( friends ) ):
    print (" ", i, ">>", friends [i])
