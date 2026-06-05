# maximum and minimum of tuple
tp = (45,23,53,53,99,0,4,8,90,-99,-34,-23,-87,-54,-12)
print("Maximum value of tuple",max(tp))
print("Minimum value of tuple",min(tp))

#Sum and average of tuple

sums = sum(tp)
ave = sum(tp)/len(tp)
print("sum of tuple: ",sums)
print("Average of tuple: ",ave)

#Ascending and reversed order of tuple

ascending = sorted(tp)
revers = reversed(tp)
print("Ascending order of: ",ascending)
print(f"Reversed order: {revers} ")

#removing duplicate tuple

new_tuple = set(tp)
print("After removing duplicates:",new_tuple)

#second largest tuple

second = sorted(tp)[-2]
print("Second largest element:",second)

#all even number
for i in tp:
    if i%2==0:
        print("all even number",i)

#positive and negative tuple 
positive = ()
negative = ()

for i in tp:
    if i>=0:
        positive += (i,)
    else:
        negative += (i,)

print("positive tuple",positive)
print("negative tuple",negative)

#number of positive and negative integers

pv = 0
nv = 0 
for i in tp:
    if i>=0:
        pv+=1       
    else:
        nv+=1        

print("Number of positive no. :",pv)
print("Number of negative no. :",nv)