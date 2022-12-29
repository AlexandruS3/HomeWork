from os import system
system("cls")

def inputInt( d ):
    c = input(d)
    return int(c)

def inputFloat( d ):
    c = input(d)
    return float(c)    

def inputBoolean( d ):
    c = input(d)
    return bool(c)


n = inputFloat("Enter the first integer: ")
m = inputFloat("Enter the second integer: ")
print(f' {n} + {m}')


