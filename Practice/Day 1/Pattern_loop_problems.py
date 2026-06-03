# for i in range(1,6): # left lean triangel
#  for j in range(i):
#     print("*",end="")
#  print()

#right lean triangel
# for i in range(1,6):
#     print(" "*(5-i) +"*"*i)

#pyramid
# for i in range(1,6):
#     print(" "*(5-i)+"* "*i)\

#inverted triangle
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    

#inverted pyramid 
# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "*i)

#dymond shape
# for i in range(1,6):
#     print(" "*(5-i)+"* "*i)

# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "*i)

#for inverted pyramid
n=5
for i in range (1,n+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
