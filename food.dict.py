# Food order
order = {
    'client'   : 'John Doe',
    'item'     : 'Salad',
    'quantity' : 5,
    'price'    : 15.00
}

deliv = input("do you need delivery? yes/no  ")
if deliv == "yes":
    order['delivery'] = 50
else:
    order['delivery'] = 0

order['total'] = order['price'] * order ['quantity'] + order['delivery']
if order['quantity'] >= 7:
    order['total'] = order['total'] - (order['total'] * 0.2)

if order['total'] >= 300 and deliv == 'yes':
    order['delivery'] = 'free'


print(order)
####################### 
print("ORDER FOR :", order['client'])
print("Food      :", order['item'])
print("Pric x qty:", order['price'], 'x', order['quantity'],'==', order['total'])
