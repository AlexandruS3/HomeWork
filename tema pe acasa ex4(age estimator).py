# Structuri de control

from os import system


system ('cls')
anul_nasterii = int(input('anul nasterii? '))
virsta = int(2022 - anul_nasterii)
if virsta < 0 :
    print ('eroare')
elif virsta <= 3 :
    print('baby,', virsta, "ani")
elif virsta <= 9 :
    print('kid,', virsta, "ani")
elif virsta <= 15 :
    print('teen,', virsta, "ani")
elif virsta <= 18 :
    print('young,', virsta, "ani")
elif virsta <= 50 :
    print('adult,', virsta, "ani")
elif 122 >= virsta > 51 :
    print('old,', virsta, "ani")
else: 
    print ('eroare')

    
