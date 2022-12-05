# bidimensional / 2 levels
from os import system
system ("cls")

destination = [
    [
        "Paris",
        "Rome",
        "London",
    ],
    [
        "NY",
        "Arizona",
        "DC",
    ]
]

print ("EU:") 
for i  in destination[0] :
   for destination[0] in i[1]:
    
    print (" -",i)    

print ("---")
print ("US:")    
for i  in destination[1] :
   for destination [1] in i[0]:
    print (" -",i)
print ("\n")
# HW1
#   * using for inside for print all destination
#   * try to make it looks so:

# EU:
#   - Paris
#   - Rome
# ---
# US:
#   - NY
#   - Toronto