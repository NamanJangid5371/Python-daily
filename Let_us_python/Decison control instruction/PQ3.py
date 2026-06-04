ms = input('Enter marital status: ')
s = input('Enter sex: ')
age = input('Enter age: ')
if(ms=='m') or (ms=='u' and s=='m' and age>30)\
or(ms=='u' and s=='f' and age>25):
    print('Insured')
else:
    print('Not insured')