iname = input("Enter your name of iteam: ")

qiteam = int(input("Enter the quntity of iteam: "))

iprice = float(input("Enter the price of iteam: "))

total_cost = qiteam*iprice

print("Recept",iname ,f"qty:{qiteam}",f"total: ${total_cost:.2f}",sep="|")
