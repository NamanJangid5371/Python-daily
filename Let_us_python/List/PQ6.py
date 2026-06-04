list = [78,-90,76,-45,-23,32,-12,23,-10,-45]

positve=[]
negative=[]


for i in list:
    if i<=0:
        negative.append(i)
    else:
        positve.append(i)
        

print("List with positive positive: ",positve)
print("List with negative numbers: ",negative)