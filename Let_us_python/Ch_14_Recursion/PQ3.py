def factorize(n,i):
    if i<=n:
        if n%i == 0:
            print(i,end = ",")
            n = n//i
        else:
            i+=1
            factorize(n,i)

            num = int(input('Enter a number:'))
            print('Prime factors are:')
            factorize(num,2)