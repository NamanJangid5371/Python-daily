t1 = (12,23,34,45,56,76,98)
t2 = (12,32,34,45,65,76,98)
tc = ()
for i in t1:
    if i in t2:
        tc += (i,)



print("new tuple with comman element:",tc)