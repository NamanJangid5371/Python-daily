name = str(input("Enter Name of student: "))
roll_no = int(input("Enter the Roll no.:"))
marks = []

for i in range(0,5):
    m = int(input(f"Enter the Marks in subject {i}:"))
    marks.append(m)

total = sum(marks)
percentage = (total/len(marks))

print("Total marks:",total)
print("Percentage:",percentage,"%")

if percentage>90:
    print("Grade A")
elif percentage>70:
    print("Grade B")
elif percentage>50:
    print("Grade C")
elif percentage>30:
    print("Fail")