# HW1: DrawLine
#  -----
# HW2: DrawLine
#    |
#    |
#    |

def drawline(d, h):                     
    for i in range(d):
        i = "-"
        if h == "h":
         print(i, end="")
        elif h == "v":
            i ="|"
            print(i)
        
drawline(5,"h")        


