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
        "Toronto",
        "DC",
    ]
]

j = 0

for i in destination:
    for destination in i:
        print (f"{j} {destination}")        
        j +=1
        
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