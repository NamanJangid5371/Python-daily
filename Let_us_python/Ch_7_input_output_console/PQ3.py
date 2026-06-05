cb = int(input("Enter the curent balance: "))
wa = int(input("Enter withdrawl amount: "))

sf = 1000

if sf<=cb and wa<=cb :
    Bl = cb-wa
    print("Current balance after withdrawl: ",Bl)
else:
    print("insusuficiant balance")
