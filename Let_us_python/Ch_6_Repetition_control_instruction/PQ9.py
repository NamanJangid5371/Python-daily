

for i in range(1,11):
    q = int(input("Number of times interest compunds: "))
    r = float(input("Rate of interest: "))
    n = int(input("number of years: "))
    p = int(input("Principal amount: "))
    a = p*(1+r/q)**(n*q)
    print("final amount: ",a)
    q+=1
    print("compounding",q)
