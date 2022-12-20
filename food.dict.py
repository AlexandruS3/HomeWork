# Food order
order = {
    'client'   : 'John Doe',
    'item'     : 'Salad',
    'quantity' : 5,
    'price'    : 15.00
}

deliv = input("do you need delivery? yes/no  ")                             #WH: question
if deliv == "yes":
    order['delivery'] = 50                                                  #HW: when total < 300.00 delivery is 50.00      
else:
    order['delivery'] = 0                                                   #HW: without delivery

order['total'] = order['price'] * order ['quantity'] + order['delivery']
if order['quantity'] >= 7:                                                  #HW: discount 20% when quantity is more than 7
    order['total'] = order['total'] - (order['total'] * 0.2)                

if order['total'] >= 300 and deliv == 'yes':                                #HW: when total > 300.00 delivery is free
    order['delivery'] = 'free'


print(order)
####################### 
print("ORDER FOR :", order['client'])
print("Food      :", order['item'])
print("Pric x qty:", order['price'], 'x', order['quantity'],'==', order['total'])
