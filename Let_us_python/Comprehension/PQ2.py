menu = {"Espresso": 2.50, "Latte": 3.50, "Croissant": 4.00, "Muffin":3.00}
inflated_menu={item: price * 1.1 for item, price in menu.items()}
for item, price in inflated_menu.iteam():
    print(f"{item}: ${price:.2f}")