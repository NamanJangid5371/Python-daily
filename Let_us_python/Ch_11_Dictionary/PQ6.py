capitals = {"India":"Delhi",
            "Pakistan":"Islamabad",
            "Shri lanka":"Sri Jayawardenepura Kotte",
            "Nepal":"Kathmandu",
            "China":"beijing",
            "Bangladesh":"Dhaka"}

country = input("Enter the name of the country: ")

if country in capitals:
    print("Capitals:",capitals[country])
else:
    print("Country not found in dictionary.")