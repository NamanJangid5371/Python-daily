string = 'Nagpur-44001099999999'
alphabet=0
digit=0

for i in string:

    if i.isalpha():
        alphabet+=1

    elif i.isdigit():
        digit+=1

print("Number of strings:",alphabet)
print("Number of digits:",digit)


