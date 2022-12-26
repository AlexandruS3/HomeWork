from os import system
from datetime import datetime

## Notes APP
#   * add new note (order)
#   * show all notes
#   * delete one

#   * timer

notes = [
    {  
        "text": "table 1, 2 soups",
        "when": "17:32 ",
    },

    {
        "text": "bill to table 2",
        "when": "15:12",
    },    
    
    {
        "text": "call mom",
        "when": None
    }    
]

def clear():
    system("cls")

def showNotes(pnotes):
    now = datetime.now()
    h, m = now.hour, now.minute
    for note in pnotes:
        warning = ""
        if note ["when"] != None:
            fragments = note["when"].split(":")                             
            nh, nm = int(fragments[0]), int(fragments[1])                       # HW2: convert formula for different time 
            if (h == nh and nm - m < 5 and nm - m > 0) or\
                 (h == nh -1 and nm-m + 60 < 5 and nm-m +60>=0):            
                  warning = "( 5 or less min left !!! )"
            
        print(f"{note['text']}{warning}")
       
def addNote(pnotes):                                                        
    text = input("enter text: ")                                                # HW1: ask the user if he wants in on a speciffic place
    idx  = int(input("where did you want to add: ")) - 1                        

    pnotes.insert(idx, { "text": text } )

def deleteNote(pnotes):
    idx = int(input("which one: ")) - 1
    pnotes.pop(idx)
   
#######################################
clear()

showNotes(notes) 

