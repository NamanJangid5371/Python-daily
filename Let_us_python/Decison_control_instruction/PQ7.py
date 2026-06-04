x1= int(input("write value of x1: "))
y1= int(input("write value of y1: "))

x2= int(input("write value of x2: "))
y2= int(input("write value of y2: "))

x3= int(input("write value of x3: "))
y3= int(input("write value of y3: "))

area = x1*(y2-y3)+ x2*(y3-y1)+ x3*(y1-y2)

if area==0:
    print("these three point are fall in straight line.")
else:
    print("thers line doesn't fall in straight line.")