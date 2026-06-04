population = 100000
new = population
for i in range(1,11):
   population = population + new*0.1
   i+=1
   print("Population in year",f"{i}","is: ",population)
