#draw swuare '+' with a given size (Kb)
from os import system
system ('cls')

size1 = int(input('size: '))
size2 = int(input('size: '))
n    = 1
lenght = size1 * size2

while n<= lenght:
    print ('+ ', end='')
    if n % size2 == 0:
        print()


    n += 1