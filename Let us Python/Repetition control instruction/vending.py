total_inserted=0.0

while total_inserted<2.5:
    
    coin= float(input("Insert the coin of value 0.10, 0.25, 1.00: "))
    if coin==0.1 or coin==0.25 or coin==1.00:

        total_inserted+=coin
        print(f"current total is = ${total_inserted:.2f}")
    else:
        print("Invalid coin! Transaction rejected for this coin")
        continue

print(f"Success Total Collected: ${total_inserted:.2f}. dispensing itema")

