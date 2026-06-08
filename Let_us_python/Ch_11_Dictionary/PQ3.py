d = {
    'anuj':{'Salary':10000,'age':20,'height':6},
    'aditya':{'Salary':6000,'age':26,'height':5.6},
    'rahul':{'Salary':7000,'age':26,'height':5.9}
}
lst = []
for v in d.values():
    lst.append(v['Salary'])

print(max(lst))
print(min(lst))