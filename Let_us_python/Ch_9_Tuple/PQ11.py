student = ((21,"Naman Jangid",75),
           (22,"Peral",90),
           (23,"Prakhar",80))

print("Student Records")
for i in student:
    print("Roll no.:",i[0],"Name of student:",i[1],"Marks:",i[2])

hmarks = student[0]

#Highest makrs 

for i in student:
    if i[2]>hmarks[2]:
        hmarks = i

print("Student with highest marks: ")
print("Name of the student: ",hmarks[1])
print("roll no.: ",hmarks[0])
print("mraks of student: ",hmarks[2])


#average marks of the student 

total_marks = 0

for i in student:
    total_marks += i[2]

average = total_marks/len(i)
print("makrs average:",average)