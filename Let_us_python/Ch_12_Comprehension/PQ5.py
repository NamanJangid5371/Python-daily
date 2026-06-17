def cal_sum_prod(x,y,z):
    sum = x + y + z
    pro = x*y*z
    
    return sum,pro

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
s,p = cal_sum_prod(a,b,c)
print(s,p)