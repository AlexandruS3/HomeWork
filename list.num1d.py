from os import system
system ("cls")

# list / array / vector
data = [ -10, 0,  5, 10, 15, 20, 0 ]

# len 
#print (f"the data has{len(data)} values")

#HW1. set zeros in the second half
half_idx = round (len(data) / 2)
print (half_idx)
for i in range (half_idx, len (data)):
    data[i] = 0

second_half = (len(data)-len(data))             #second half
for i in range (second_half,half_idx):     #-------HW1---------
    data[i] = 0
#HW3: do the same but for the left half


#  Swapping
# HW2: input indexes of values from kb

data5 = input("introdu 2 numere ")
f = data5.split() 
data[1] = f[0]                                   #swapping
f[0] = data [4]                            #-------HW2---------
data[4] = f[1]
f[1] = data[1]
print (data)

#HW3: find the max/min values and print
v_min = data[0]
for i in data:
    if i < v_min:
        v_min = i                                #min/max
print (v_min)                              #-------HW3---------

v_max = data[0]
for i in data:
    if i > v_max:
        v_max = i
print (v_max)    



 