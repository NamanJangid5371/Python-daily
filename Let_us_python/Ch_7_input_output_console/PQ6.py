price = []

for i in range(1,11):
    ip=int(input(f"Etner the price of iteam no.{i}:"))
    price.append(ip)

print("Total bill:",sum(price))
print("Highest price iteam:",max(price))
print("Lowest price iteam:",min(price))
print("Average price iteam:",sum(price)/len(price))
