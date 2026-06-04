list = [55,65,76,55,98,67,76,98]

list_new = []

for item in list:
    if item not in list_new:
        list_new.append(item)

        print("Original list:",list)
        print("New list after removing duplicate item:",list_new)
        