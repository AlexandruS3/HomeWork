from os import system
system("cls")

def wrap_brackets( text ):
  return "(" + text + ")"
                                               
def square_bracket( text ):
  return "[" + text + "]"           #HW  <<<[[[(12345)]]]>>>
  
def greather_than( text ):
  return "<" + text + ">"  

print(greather_than(greather_than(greather_than(square_bracket\
    (square_bracket(square_bracket(wrap_brackets("12345"))))))))
   




