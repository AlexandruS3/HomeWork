from os import system

user = {
    'username': 'johny77',
    'online'  : True,
    'email'   : 'johny77lucky.me',
    'rating'  : 7777777,

    'friends' : [
        'marry888',
        'candy001',
        'peter99'
    ]
}

#while True:
#   name = input(" name friends: ")
#    if name == "":
#        break
#    user['friends'].append(name)
system("cls")
print(user['username'])
print(user['email'])
############################################
if user['rating'] == 0 :
 print("No Likes")
elif user['rating'] <= 999  :
 print(user['rating'], "Likes")
elif user['rating'] < 1000000 :
    if user['rating'] < 10000:
        print (str(user['rating'])[:1]+"k", "Likes")
    elif user['rating'] < 100000:
        print (str(user['rating'])[:2]+"k", "Likes")
    else:
        print (str(user['rating'])[:3]+"k", "Likes")
elif user['rating'] < 1000000000 :
    if user['rating'] < 10000000:
        print (str(user['rating'])[:1]+"."+str(user['rating'])[1:2]+"M", "Likes")
    elif user['rating'] < 100000000:
        print (str(user['rating'])[:2]+"."+str(user['rating'])[2:3]+"M", "Likes")
    else:
        print (str(user['rating'])[:3]+"M", "Likes")
elif user['rating'] < 10000000000 :
        print (str(user['rating'])[:1]+"T", "Likes")





#############################################
print('FRIENDS LIST:')
for i in range ( len(user['friends']) ):
    print('>>',user['friends'][i])



# HW1 : add some moere friends from keyboard <- input + loop
#       hint: list.append("value") ))
# HW2: if+else - artihmetic:
#      user['rating']  0 .. 10 000 000 000
#      0 -> No likes
#      1..999 -> 999 Likes
#      1000 ... 100000-> (123456) -> 123k Likes
#      1000000+ .. 1000 000 000 -> M xx.xxLikes
#       1000 000 000 .. 10 000 000 000 -> T xx.xxLikes