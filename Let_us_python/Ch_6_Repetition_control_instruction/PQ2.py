lst = ['desert','dessert','to','too','lose','loose']
s = 'Mumbai'
for i in range(len(lst)):
    if i>3:
        break
    else:
        print(i,lst[i],s[i])
        i+=1