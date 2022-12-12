from os import system
system ("cls")

people = [ "Marry", 20, "John", 21, "Peter", 21]        # ---EX1---
n = 0
for i in range (len(people)):
    if (type(people[i])) is str: 
        n +=1
print (n)                                               # ---EX2---
#####
people_names = []                                       # ---EX4---
people_ages  = []

for i in range (len(people)):
    if (type(people[i])) is str:
     people_names.append(people[i])                     # ---EX5---
    elif (type(people[i])) is not str:
     people_ages.append(people[i])



x = input("choose person: ")
if x == '0':
    print(people_names[0], people_ages[0])
elif x == "1":
    print(people_names[1], people_ages[1])              # ---EX6---
elif x == "2":
    print(people_names[2], people_ages[2])    
else: 
    print ("this person does not exist")

x = input("name: ")     
if x == "Marry":
    print (people_ages[people_names.index(x)])
elif x == "John":                                       # ---EX7---
    print (people_ages[people_names.index(x)])
elif x == "Peter":
    print (people_ages[people_names.index(x)])
else:
    print ("this person does not exist")        

x = input("name and age for change: ")
w = x.split()
d = int(w[1])
if w[0] == "Marry":
    people_ages.pop(0)
    people_ages.insert(0, d)                            # ---EX8---
if w[0] == "John":
    people_ages.pop(1)
    people_ages.insert(1, d)
if w[0] == "Peter":
    people_ages.pop(2)
    people_ages.insert(2, d)

x = input("name for eliminate: ")
y =people_names.index(x)
people_names.pop(y)                                    # ---EX9---
people_ages.pop(y)


x = input("add new name ang age: ")
w = x.split()
people_names.append(w[0])                               # ---EX10---
people_ages.append(w[1])


x = input("name ang age for start list: ")
w = x.split()
people_names.insert(0, w[0])                            # ---EX11---
people_ages.insert(0, w[1])

print(people_ages, people_names)







   

    
        
    
                
          
 