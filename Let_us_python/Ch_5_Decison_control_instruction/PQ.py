qty = int(input('enter value of quantity:'))
price = float(input('enter value of price:'))

if qty>1000:
    dis=10
else:
    dis=0
totexp = qty*price-qty*price*dis/100
print('Total expenses = Rs.'+str(totexp))