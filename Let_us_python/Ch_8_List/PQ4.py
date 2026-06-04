list = [23,42,12,43,53,55,87,98,87,67,12,42,57,39,39,58,34,23,12,87]
num = int(input("Enter the number to search: "))

Found = False

for i in range(len(list)):
    if list[i]==num:
        print("Found at position: ", i+1)
        Found=True
        if not Found:
            print("The number is not in the list.")
