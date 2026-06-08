stinfo = {554:'Ajay',350:'Ramesh',359:'Rakesh'}
rollno = int(input('Enter roll number:'))
name = stinfo.get(rollno,'Student')
print(f'Congratulations {name}!')
rollno = int(input('Enter roll number:'))
name = stinfo.get(rollno,'Student')
print(f'Congratulations {name}!')