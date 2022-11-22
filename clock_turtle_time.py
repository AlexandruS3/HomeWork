# data
import turtle as t
hours   = 4
minutes = 55
seconds  = 30

# print the time 
def printTime():
    print ( f"{hours:02}:{minutes:02}:{seconds:02}") 

# draw clock with turtle
def drawClock():
    t.circle(100)
    t.fillcolor("red")
    t.left(90)
    t.penup()
    t.forward(100)
input ("Hit enter to exit")
def drawhour():    # hours indicator
    t.pensize(5)
    t.pendown()
    t.right(hours * 30)
    t.color("orange")
    t.forward(70)
   

    # reset the pen
    t.penup
    t.left(180)
    t.forward(70)
    t.right(180 -hours * 30)

def drawminute():   # minute indicator
    t.pensize(2)
    t.pendown()
    t.right(minutes * 6)
    t.color("green")
    t.forward(90)

    # reset pen
    t.penup
    t.left(180)
    t.forward(90)
    t.right(180 -minutes *6)

def drawsecond():   # seconds indicator
    t.pensize(1)
    t.pendown()
    t.right (seconds * 6)
    t.color("pink")
    t.forward(98) 


    # HW1: contunue drawing the seconds indicator
    # try anower color
    # try another way of drawing
    # HW3: try to make 3 different function1
    input ("Hit enter to exit")