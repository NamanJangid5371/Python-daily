def sanitize_list(list):
    new_list = []

    for iteam in list:
        if iteam not in new_list:
            new_list.append(iteam)


numbers = [1,2,3,4,5,6,6,5,4,8,9]

result = sanitize_list(numbers)

print(result)
