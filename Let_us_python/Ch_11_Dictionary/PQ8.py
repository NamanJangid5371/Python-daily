phonebook = {}

while True:
    print("\nPhonebook Menu")
    print("1. Add contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        phonebook[name] = number
        print("Contact added successfully!")

    elif choice == 2:
        name  = input("Enter name to search: ")
        if name in phonebook:
            print("Phone Number:",phonebook[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter the name to update: ")
        if name in phonebook:
            number = input("Enter the new number: ")
            phonebook[name]=number
            print("Number updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter the name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found")

    elif choice == 5:
        print("\nAll Contacts:")
        for name, number in phonebook.items():
            print(name,":",number)

    elif choice == 6:
        print("Exiting Phonebook...")
        break
    else:
        print("Invalid choice")

