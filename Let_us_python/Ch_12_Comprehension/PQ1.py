guests = [("Alice",25),("Bob",17),("Charlie",32),("David",15),("Eva",21)]
vip_lounge={name for name, age in guests if age >=21}
print("VIP Lounge guests:", vip_lounge)