## app <--- two integers <--- user
##     <--- choose operations <--- user
##          display result --->


def ii (which):
    print("Enter", which,"integer:  ", end= "")
    return int(input())

a = ii("firs")
b = ii("second")

op = input("Choose operations (* / + - **): ") #op = "+"

res = 0

if op == "+":
    res = a + b                             # HW1 : operations + * / - **
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
elif op == "-":
    res = a - b
elif op == "**":
    res = a ** b
else:                                       # HW2: if the user choses an inexistent operations
    print(" >> wrong operation")            #       >> wrong operations

print("Result: ", res)