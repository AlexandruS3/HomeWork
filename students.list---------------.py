from os import system
system ("cls")

students_first_name = []
students_last_name  = []
students_age        = []
students_mark       = []
age                 = list(range(18,30))
mark                = list(range(1,10))

while len (students_first_name) < 100 :
    data = input("Enter student's data:  ")
    if data == "":
        break
    
    x = data.split() 
 
    if x[2] in age or x[3] in mark:
    
        students_first_name.append(x[0])
        students_last_name.append(x[1])
        students_age.append(x[2]) 
        students_mark.append(x[3])
    
    
for i in range (len(students_first_name)):
    print (i,students_first_name[i], students_last_name[i], students_age[i],students_mark[i])
       
