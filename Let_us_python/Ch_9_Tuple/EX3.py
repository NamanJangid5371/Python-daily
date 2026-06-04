list = [
    ("Mouse",200),
    ("Keyboard",500),
    ("CPU",25000),
    ("Monitor",10000),
    ("Speakers",1000)
]

sorted_items = sorted(list, key=lambda x: x[1], reverse= True)

print("new list after sorted price:")

for item, price in sorted_items:
    print(item,"-",price)