# APP---> waiters
# ONE WAITER ---> 3 tables
from os import system
system ("cls")

food_name  = ["Pizza", "Salad", "Soup"]
food_price = [ 100.00,  50.00,   25.00]

status = ["free", "free", "free" ]
client = [    "",     "",     "" ]
order  = [    "",     "",     "" ]
bill   = [   0.0,    0.0,    0.0 ]
tip    = [   0.0,    0.0,    0.0 ]
while len(food_name)<100:
# 1. clinet "John" --> 3rd table
    name = input("write client name: ")
    if name == "":
        break
    x    = name.split()
    client[2] = x[2]
    status[2] = "not-free"

    client[0] = x[0]
    status[0] = "not-free"

    # 2. "John" orders a soup
    client_name = client[2]
    food_order_name = input ("choose food: Pizza or Salad or Soup: ")
    
    #HW2: try to add input from kb
    client_idx   = client.index(client_name)
    # print(clinet_idx)
    order[client_idx] = food_order_name
    food_idx = food_name.index(food_order_name)
    bill[client_idx]  = food_price[food_idx]
    tip[client_idx]   = bill[client_idx] *0.1

for ti in range(len(status)):
    print(f"table {ti+1} ({status[ti]}):")
    if status[ti] != "free":
        print (f"\t {client[ti]}")
        # HW1: do not show this if no order 
        # ->0.0
        if order[ti] != "":
         print(f"\t {order[ti]}->{bill[ti]} % {tip[ti]}")


