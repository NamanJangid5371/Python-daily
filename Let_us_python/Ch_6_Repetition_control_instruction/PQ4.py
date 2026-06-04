num = int(input("Enter the the numbers:"))

original=num
reverse=0

while num>0:
    digit = num%10
    reverse = reverse*10 + digit
    num = num // 10

    print("Reversed numbere:",reverse)

    if original==reverse:
        print("Ther numbers are different.")
    else:
        print("The numbers are same.")
