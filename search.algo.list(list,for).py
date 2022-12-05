# SEARCH ALGO VARIANTS:
# is the item in the container???
# - iterate
# - compare (exact/approximation)
# - remember

items      = ["Marry", "Peter"]
found      = [ False ,  False]
container  = ["John", "Marry", "Bob"]

for j in range( len (items)):
    for i in range(len(container)):
        found[j] = container[i] == items[j]
        if found[j]:
            break
    
    
print (items) 
print (found)  
for j in range(len(items)):    
    if found:
        print(items, "FOUND!")
    else:
        print(items, "NOT FOUND!")        
