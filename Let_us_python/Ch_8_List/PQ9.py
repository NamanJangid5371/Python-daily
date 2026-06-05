l1=[23,34,45,56,67,87,98,0]
l2=[32,23,43,34,56,65,98,23]

l3=[]

for i in l1:
    if i in l2:
        l3.append(i)
        print("New list with comman element:",l3)