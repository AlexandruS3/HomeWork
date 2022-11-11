# draw this triangle

# . . +             0  2/1
# . + + +           1  1/3
# + + + + +         2  0/5

from os import system
system ("cls")
x = int(input ('what size of triangle do you want ?  '))
n = 0
while n < x :
    print ('. ' *(x-n), '+ '*(2*n+1)   )
    n +=1
print(' \n\n ')
print ('Enjoy your triangle :)')
print(' \n\n ')