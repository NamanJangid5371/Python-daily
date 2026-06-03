bs = int(input('Enter value of bs: '))
if bs<1500:
    hra = bs*10/100
    da = bs*90/100
else:
 hra = 500 
 da = bs* 98/100
gs=bs+da+hra
print('Gross Salary = Rs.'+str(gs))