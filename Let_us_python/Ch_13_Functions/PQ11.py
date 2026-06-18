def print_it(i,a,s,*args):
    print()
    print(i,a,s,end = '')
    for var in args:
        print(var,end='')

print_it(10,3.14,5)
print_it(20,s='Hi',a=6.28)
print_it(a=6.28,s='Hello',i=30)
print_it(40,2.35,'Nag','Mum',10)
