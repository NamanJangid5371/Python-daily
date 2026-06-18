def create_list(list1,list2):
    intersection = []

    for item in list1:
        if item in list2:
            intersection.append(item)

    return intersection

a = [1,2,3,4,5]
b = [3,4,5,6,7]

result = create_list(a,b)
print(result)