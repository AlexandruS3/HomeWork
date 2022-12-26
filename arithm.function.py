# create a function that corespond to: * / + -

# pure function
def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def min(a,b):
    return a - b                        # Hw1 create a function that corespond to: * / + -

def sum(a,b):
    return a + b 
   
#HW2: rewrite: r= 1 + 2 * 3 / 4
r = sum(15, 45)
print(r)



def sum2(a,b):
    return a + b 

def mul2(a,b):
    return a * b

   
def div2(a,b):
    return a / b

def calcul():
    w=sum2(1, mul2(2, div2(3,4)))       # Hw2 rewrite: r= 1 + 2 * 3 / 4
    return w
print(calcul())